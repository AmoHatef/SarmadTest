from bale import Bot, Message
bot = Bot (token = '1618506529:jgujgqcOf2M866wp__AL-04ft183EA8mm2Q')
Hatef = ['1478' , 'نامحدود' , 'نامحدود']
ParhamHatami = ['parham1392' , '500' , '50000']
𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊 = ['????' , '400' , '9014.73']
AriyaMotamed = ['ariagoogooli' , '175' , '0']
Amirzone91 = ['algogolariyala' , '1000' , '0']
kianganenet = ['k139101391k' , '225' , '93.87']
atila = ['At!l@1392' , '1225' , '0']
Parsa = ['727727276234' , '875' , '400000']
mahan165 = ['mahan.165' , '1425' , '0']
hatef = 1652444615
amo = 1311998189
radnik = 282784158
ariya = 48491883
admins = [hatef , amo , radnik , ariya]
proadmins = [radnik , hatef]
name = 0
A = 1
marhale = 0
@bot.event
async def on_message(pm = Message):
    global A
    global karbar
    global marhale
    if A == 1:
        print ('Bot runned')
    else:
        if pm.content == ('عمو'):
            await pm.reply('من عمو نیستم ولی میتونی پیامت رو برام بفرستی تا به دست عمو برسونم')
        elif pm.content == ('هاتف'):
            await pm.reply('من هاتف نیستم ولی میتونی پیامت رو برام بفرستی تا به دست هاتف برسونم')
        elif pm.content.lower() == '/getgift':
            await pm.reply('Working...')
        elif pm.content.lower().startswith('/offer'):
            await pm.reply('پیشنهاد شما برای ادمین های سرور ارسال شد.✅\nدر صورت تایید شدن پیشنهاد، مبلغ پاداش در همین چت ارسال خواهد شد.🎁')
            for i in range (len(admins)):
                await bot.send_message(chat_id = admins[i], text = pm.content)
        elif pm.content == ('ورود به اکانت'):
            if pm.chat_id == 4360392520:
                await pm.reply('*ورود به اکانت از طریق گروه ممکن نیست.❌\nبرای ورود به اکانت: @Sarmad_Test_bot*')
            else:
                if marhale == 3:
                    await pm.reply('شما از قبل در یک اکانت وارد شده اید.❌\nبرای خروج: *خروج از اکانت*')
                if marhale == 0:
                    marhale = 1
                    await pm.reply('نام کاربری خود را درون سینگل کوتیشن وارد کنید.')
        elif (pm.content == "'Hatef'" or pm.content == "'ParhamHatami'" or pm.content == "'𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊'" or pm.content == "'AriyaMotamed'" or pm.content == "'Amirzone91'" or pm.content == "'kianganenet'" or pm.content == "'atila'" or pm.content == "'Parsa'") and marhale == 1:
            await pm.reply('رمز عبور خود را وارد کنید.🔑')
            global name
            name = pm.content
            marhale = 2
        elif (pm.content != "'Hatef'" or pm.content != "'ParhamHatami'" or pm.content != "'𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊'" or pm.content != "'AriyaMotamed'" or pm.content != "'Amirzone91'" or pm.content != "'kianganenet'" or pm.content != "'atila'" or pm.content != "'Parsa'") and marhale == 1:
            await pm.reply('هیچ اکانتی با نام کاربری وارد شده در سرور وجود ندارد.❌')
        if name == "'Hatef'" and pm.content == Hatef[0] and marhale == 2:
            Hatef.insert(1, pm.chat_id)
            marhale = 3
            await pm.reply('ورود به اکانت Hatef با موفقیت انجام شد.✅')
        elif name == "'Hatef'" and pm.content != Hatef[0] and marhale == 2 and (pm.content != "'Hatef'" and pm.content != "'ParhamHatami'" and pm.content != "'𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊'" and pm.content != "'AriyaMotamed'" and pm.content != "'Amirzone91'" and pm.content != "'kianganenet'" and pm.content != "'atila'" and pm.content != "'Parsa'"):
            await pm.reply('رمز عبور نادرست میباشد.❌')
        if name == "'ParhamHatami'" and pm.content == ParhamHatami[0] and marhale == 2:
            ParhamHatami.insert(1, pm.chat_id)
            marhale = 3
            await pm.reply('ورود به اکانت ParhamHatami با موفقیت انجام شد.✅')
        elif name == "'ParhamHatami'" and pm.content != ParhamHatami[0] and marhale == 2 and (pm.content != "'Hatef'" and pm.content != "'ParhamHatami'" and pm.content != "'𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊'" and pm.content != "'AriyaMotamed'" and pm.content != "'Amirzone91'" and pm.content != "'kianganenet'" and pm.content != "'atila'" and pm.content != "'Parsa'"):
            await pm.reply('رمز عبور نادرست میباشد.❌')
        if name == "'𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊'" and pm.content == 𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊[0] and marhale == 2:
            𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊.insert(1, pm.chat_id)
            marhale = 3
            await pm.reply('ورود به اکانت 𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊 با موفقیت انجام شد.✅')
        elif name == "'𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊'" and pm.content != 𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊[0] and marhale == 2 and (pm.content != "'Hatef'" and pm.content != "'ParhamHatami'" and pm.content != "'𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊'" and pm.content != "'AriyaMotamed'" and pm.content != "'Amirzone91'" and pm.content != "'kianganenet'" and pm.content != "'atila'" and pm.content != "'Parsa'"):
            await pm.reply('رمز عبور نادرست میباشد.❌')
        if name == "'AriyaMotamed'" and pm.content == AriyaMotamed[0] and marhale == 2:
            AriyaMotamed.insert(1, pm.chat_id)
            marhale = 3
            await pm.reply('ورود به اکانت AriyaMotamed با موفقیت انجام شد.✅')
        elif name == "'AriyaMotamed'" and pm.content != AriyaMotamed[0] and marhale == 2 and (pm.content != "'Hatef'" and pm.content != "'ParhamHatami'" and pm.content != "'𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊'" and pm.content != "'AriyaMotamed'" and pm.content != "'Amirzone91'" and pm.content != "'kianganenet'" and pm.content != "'atila'" and pm.content != "'Parsa'"):
            await pm.reply('رمز عبور نادرست میباشد.❌')
        if name == "'Amirzone91'" and pm.content == Amirzone91[0] and marhale == 2:
            Amirzone91.insert(1, pm.chat_id)
            marhale = 3
            await pm.reply('ورود به اکانت Amirzone91 با موفقیت انجام شد.✅')
        elif name == "'Amirzone91'" and pm.content != Amirzone91[0] and marhale == 2 and (pm.content != "'Hatef'" and pm.content != "'ParhamHatami'" and pm.content != "'𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊'" and pm.content != "'AriyaMotamed'" and pm.content != "'Amirzone91'" and pm.content != "'kianganenet'" and pm.content != "'atila'" and pm.content != "'Parsa'"):
            await pm.reply('رمز عبور نادرست میباشد.❌')
        if name == "'kianganenet'" and pm.content == kianganenet[0] and marhale == 2:
            kianganenet.insert(1, pm.chat_id)
            marhale = 3
            await pm.reply('ورود به اکانت kianganenet با موفقیت انجام شد.✅')
        elif name == "'kianganenet'" and pm.content != kianganenet[0] and marhale == 2 and (pm.content != "'Hatef'" and pm.content != "'ParhamHatami'" and pm.content != "'𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊'" and pm.content != "'AriyaMotamed'" and pm.content != "'Amirzone91'" and pm.content != "'kianganenet'" and pm.content != "'atila'" and pm.content != "'Parsa'"):
            await pm.reply('رمز عبور نادرست میباشد.❌')
        if name == "'atila'" and pm.content == atila[0] and marhale == 2:
            atila.insert(1, pm.chat_id)
            marhale = 3
            await pm.reply('ورود به اکانت atila با موفقیت انجام شد.✅')
        elif name == "'atila'" and pm.content != atila[0] and marhale == 2 and (pm.content != "'Hatef'" and pm.content != "'ParhamHatami'" and pm.content != "'𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊'" and pm.content != "'AriyaMotamed'" and pm.content != "'Amirzone91'" and pm.content != "'kianganenet'" and pm.content != "'atila'" and pm.content != "'Parsa'"):
            await pm.reply('رمز عبور نادرست میباشد.❌')
        if name == "'Parsa'" and pm.content == Parsa[0] and marhale == 2:
            Parsa.insert(1, pm.chat_id)
            marhale = 3
            await pm.reply('ورود به اکانت Parsa با موفقیت انجام شد.✅')
        elif name == "'Parsa'" and pm.content != Parsa[0] and marhale == 2 and (pm.content != "'Hatef'" and pm.content != "'ParhamHatami'" and pm.content != "'𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊'" and pm.content != "'AriyaMotamed'" and pm.content != "'Amirzone91'" and pm.content != "'kianganenet'" and pm.content != "'atila'" and pm.content != "'Parsa'"):
            await pm.reply('رمز عبور نادرست میباشد.❌')
        elif pm.content == ('خروج از اکانت'):
            if pm.from_user.id == Hatef[1]:
                Hatef.remove

        elif pm.content == ('موجودی سرمد') or pm.content == ('موجودی صرمد') or pm.content == ('موجودی ثرمد'):
            if pm.from_user.id == Hatef[1]:
                await pm.reply(Hatef[2])
            elif pm.from_user.id == ParhamHatami[1]:
                await pm.reply(ParhamHatami[2])
            elif pm.from_user.id == 𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊[1]:
                await pm.reply(𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊[2])
            elif pm.from_user.id == AriyaMotamed[1]:
                await pm.reply(AriyaMotamed[2])
            elif pm.from_user.id == Amirzone91[1]:
                await pm.reply(Amirzone91[2])
            elif pm.from_user.id == kianganenet[1]:
                await pm.reply(kianganenet[2])
            elif pm.from_user.id == atila[1]:
                await pm.reply(atila[2])
            elif pm.from_user.id == Parsa[1]:
                await pm.reply(Parsa[2])
            else:
                await pm.reply('*شما هنوز در اکانت خود لاگین نکرده اید.❌*\n\nبرای لاگین در اکانت خود میبایست به @Sarmad_Test_bot بروید و عبارت "ورود به اکانت" را وارد کنید.📱\n\n در صورتی که هنوز برای اکانت خود رمز عبور در ربات را انتخاب نکردید، به @AmoHatef رفته و رمز عبور جدید خود را انتخاب نمایید.💻')
        elif pm.content == ('موجودی پارس') or pm.content == ('موجودی پارص') or pm.content == ('موجودی پارث'):
            if pm.from_user.id == Hatef[1]:
                await pm.reply(Hatef[3])
            elif pm.from_user.id == ParhamHatami[1]:
                await pm.reply(ParhamHatami[3])
            elif pm.from_user.id == 𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊[1]:
                await pm.reply(𝑨𝒎𝒊𝒓𝒓𝒆𝒛𝒂_𝒚𝒂𝒎𝒂𝒉𝒅𝒊[3])
            elif pm.from_user.id == AriyaMotamed[1]:
                await pm.reply(AriyaMotamed[3])
            elif pm.from_user.id == Amirzone91[1]:
                await pm.reply(Amirzone91[3])
            elif pm.from_user.id == kianganenet[1]:
                await pm.reply(kianganenet[3])
            elif pm.from_user.id == atila[1]:
                await pm.reply(atila[3])
            elif pm.from_user.id == Parsa[1]:
                await pm.reply(Parsa[3])
            else:
                await pm.reply('*شما هنوز در اکانت خود لاگین نکرده اید.❌*\n\nبرای لاگین در اکانت خود میبایست به @Sarmad_Test_bot بروید و عبارت "ورود به اکانت" را وارد کنید.📱\n\n در صورتی که هنوز برای اکانت خود رمز عبور در ربات را انتخاب نکردید، به @AmoHatef رفته و رمز عبور جدید خود را انتخاب نمایید.💻')
         
        #else:
            #await pm.reply('عمو نوری عابد موحریبون')

    A = 0
if __name__ == "__main__":
    bot.run()
