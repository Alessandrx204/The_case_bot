import asyncio
import os
import aiosqlite
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
#Alssandrx 2025 all rights reserved unless specified otherwise upon request
DA_TOKEN = 'THY TOKEN HERE'
bot = Bot(DA_TOKEN)
dp = Dispatcher()
DB_PATH = os.path.join(os.path.dirname(__file__), 'the_casebot_database.db')
custom_id = 'REPLACE WITH YOUR OR SOMEONE ELSE ID FOR A CUSTOM START MESSAGE'
Special_msg = 'WRITE A CUSTOM WELCOM MSG'

# Initialise the DB
async def init_db():
    async with aiosqlite.connect(DB_PATH) as db: #aiosqlite is asyncronus sql
        await db.execute('''
            CREATE TABLE IF NOT EXISTS people_using_the_bot (
                indice INTEGER PRIMARY KEY AUTOINCREMENT,
                id TEXT UNIQUE,
                username TEXT,
                mode INTEGER
            )
        ''')
        await db.commit()

# 特別なコマンド
async def first_process_command(command: str, message: types.Message, id) -> int | None:
    match command:
        case "help":
            await message.answer("if you feel like you need help, go figure it out yourself.")
        case "capitalize":
            await message.answer("It's 'CapitaliSe' thou uneducated yankee, now vanish and go learn proper english...")
        case "langjp":
            await message.answer("Language sucessfully  not set to Japanese.")
        case "langde":
            await message.answer("Language sucessfully not set to German.")
        case "langru":
            await message.answer("Language sucessfully not set to Russian.")
        case "langen":
            await message.answer("Language sucessfully set to English.")
        case 'start':
            welcome = (
                Special_msg
                if id == custom_id  #thy
                else "Welcome to this stupid bot."
            )
            await  message.answer(welcome)
        case "lowercase" | "lower":
            return 1000
        case "uppercase" | "upper":
            return 2000
        case "capitalise":
            return 3000
        case _:
            await message.answer("Invalid command, you idiot.")

# start comman and commsnds dp.message is the thing that handles messages
@dp.message(F.text.regexp(r"^/\w+")) # ^ means start with, \w is a metacharacter stands for wordcharacter + == more than 1
async def handle_commands(message: types.Message):
    user_id = str(message.from_user.id)
    username = message.from_user.username or "ナシ"
    user_cmd = message.text[1:].lower()
    #print("✅ Function gonna be called update_db ", flush=False)
    
    mode = await first_process_command(user_cmd, message, user_id) #the mode is equal to the exit code of the function
    #print("✅ Function update_db was called", flush=False)
    if mode is None:
        return
    else:
        await update_db(user_id, username, mode)





async def update_db(id, username, selected_mode):
    print(f"[DB] Saving: {id=}, {username=}, {selected_mode=}")  # 👈 TEST ROW
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            INSERT INTO people_using_the_bot (id, username, mode)
            VALUES (?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET username=excluded.username, mode=excluded.mode
        ''', (id, username,selected_mode))  # why not F string thou may ask, well turns out people can do sql injection thru that
        await db.commit()  # saves changes of da db
        print(f" the mode has been saved to {selected_mode} :3.\n")  # excluded means instead of raising error u
        # ON CONFLICT(id): if id already exist, update username and mode with new values ( excluded are the new values from insert)
        #--------------------------------------------
        async with db.execute("SELECT * FROM people_using_the_bot") as cursor:
            rows = await cursor.fetchall()
            print(f"Number of rows : {len(rows)}")

            # Print each row
            for row in rows:
                print(row)



# normal messages
@dp.message(F.text)
async def echo_mode(message: types.Message):
    print("echo_mode as been used")
    user_id = str(message.from_user.id)
    og_text = message.text

    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT mode FROM people_using_the_bot WHERE id = ?", (user_id,)) as cursor:
            row = await cursor.fetchone()
            mode = row[0] if row else 1000  # default lowercase
            

    match mode:
        case 1000:
            msg = og_text.lower()
        case 2000:
            msg = og_text.upper()
        case 3000:
            msg = og_text.capitalize()
        case _:
            msg = og_text

    await message.answer(msg)

# Main
async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

#Alssandrx 2025 all rights reserved unless specified otherwise upon request