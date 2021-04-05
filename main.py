import discord
import smtplib
from discord.utils import get
from discord.ext import commands
import mysql.connector


mydb = mysql.connector.connect(host="localhost", user="root", password="14147714", database="vinamradb")

mycursor = mydb.cursor()


def mailer(data, reciever, subject):
    message = data
    sender = "pokemongo1003player@gmail.com"
    password = "14147714"
    body = 'Subject: {}\n\n{}'.format(subject, message)
    with smtplib.SMTP("smtp.gmail.com", 587) as smtpserver:
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(sender, password)
        smtpserver.sendmail(sender, reciever, body)



TOKEN = "ODE2Njg5MTQ1NjczNTQ3Nzg2.YD-nCQ.vaACh6IGeVwulyjJQ06ic-gdTLc"
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("bot is ready to takeoff")

@client.command(help="make new private channel")
async def make_channel(ctx):
    guild = ctx.guild
    member = ctx.author
    admin_role = get(guild.roles, name="Admin")
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        member: discord.PermissionOverwrite(read_messages=True),
        admin_role: discord.PermissionOverwrite(read_messages=True)
        }
    channel = await guild.create_text_channel('Private', overwrites=overwrites)
    await channel.send("Welcome")

@client.command(help="make new public channel")
async def make_new(ctx):
    guild = ctx.guild
    member = ctx.author
    admin_role = get(guild.roles, name="Admin")
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=True),
        member: discord.PermissionOverwrite(read_messages=True),
        admin_role: discord.PermissionOverwrite(read_messages=True)
        }
    wachannel = await guild.create_text_channel('Public', overwrites=overwrites)
    await wachannel.send("Welcome")

@client.command(aliases=['Send_mail', 'SEND_MAIL'],help='send_mail <message> <receiver_address> <subject> Admins only')
@commands.has_permissions(manage_guild=True)
async def send_mail(ctx, data, reciever, subject):
    files = open("editor.txt", "w")
    files.write(data)

    mailer(data, reciever, subject)
    await ctx.send("message sent")


@client.command(aliases=['marks5'],help='Marks5 <subject_name> <chapter_name> <topic_name> <question> (command to add 5mark questions)')
async def Marks5(ctx,subject:str,chapter:str,topic:str, *, data):
    await ctx.send("pending")
    sql = "INSERT INTO Question5Marks (subject,chapter,topic,questions) VALUES (%s,%s,%s,%s)"
    val = [subject,chapter,topic,data]
    mycursor.execute(sql, val)
    mydb.commit()
    await ctx.send("Question Added")

@client.command(aliases=['marks4'],help='Marks4 <subject_name> <chapter_name> <topic_name> <question> (command to add 4mark questions)')
async def Marks4(ctx,subject:str,chapter:str,topic:str, *, data):
    await ctx.send("pending")
    sql = "INSERT INTO Question4Marks (subject,chapter,topic,questions) VALUES (%s,%s,%s,%s)"
    val = [subject,chapter,topic,data]
    mycursor.execute(sql, val)
    mydb.commit()
    await ctx.send("Question Added")

@client.command(aliases=['marks3'],help='Marks3 <subject_name> <chapter_name> <topic_name> <question> (command to add 3mark questions)')
async def Marks3(ctx,subject:str,chapter:str,topic:str, *, data):
    await ctx.send("pending")
    sql = "INSERT INTO Question3Marks (subject,chapter,topic,questions) VALUES (%s,%s,%s,%s)"
    val = [subject,chapter,topic,data]
    mycursor.execute(sql, val)
    mydb.commit()
    await ctx.send("Question Added")

@client.command(aliases=['marks2'],help='Marks2 <subject_name> <chapter_name> <topic_name> <question> (command to add 2mark questions)')
async def Marks2(ctx,subject:str,chapter:str,topic:str, *, data):
    await ctx.send("pending")
    sql = "INSERT INTO Question2Marks (subject,chapter,topic,questions) VALUES (%s,%s,%s,%s)"
    val = [subject,chapter,topic,data]
    mycursor.execute(sql, val)
    mydb.commit()
    await ctx.send("Question Added")

@client.command(aliases=['marks1'],help='Marks1 <subject_name> <chapter_name> <topic_name> <question> (command to add 1mark questions)')
async def Marks1(ctx,subject:str,chapter:str,topic:str, *, data):
    await ctx.send("pending")
    sql = "INSERT INTO Question1Marks (subject,chapter,topic,questions) VALUES (%s,%s,%s,%s)"
    val = [subject,chapter,topic,data]
    mycursor.execute(sql, val)
    mydb.commit()
    await ctx.send("Question Added")



@client.command(aliases=['Show_mark5', 'Show_Mark5', 'SHOW_MARK5'],help='show_mark5 (returns only one random 5marks questions)')
async def show_mark5(ctx):
    mycursor.execute("SELECT questions FROM Question5Marks ORDER BY RAND() LIMIT 1;")
    myresult = mycursor.fetchone()
    await ctx.send(myresult)

@client.command(aliases=['Show_mark4', 'Show_Mark4', 'SHOW_MARK4'],help='show_mark4 (returns only one random 4marks questions)')
async def show_mark4(ctx):
    mycursor.execute("SELECT questions FROM Question4Marks ORDER BY RAND() LIMIT 1;")
    myresult = mycursor.fetchone()
    await ctx.send(myresult)

@client.command(aliases=['Show_mark3', 'Show_Mark3', 'SHOW_MARK3'],help='show_mark3 (returns only one random 3marks questions)')
async def show_mark3(ctx):
    mycursor.execute("SELECT questions FROM Question3Marks ORDER BY RAND() LIMIT 1;")
    myresult = mycursor.fetchone()
    await ctx.send(myresult)

@client.command(aliases=['Show_mark2', 'Show_Mark2', 'SHOW_MARK2'],help='show_mark2 (returns only one random 2marks questions)')
async def show_mark2(ctx):
    mycursor.execute("SELECT questions FROM Question2Marks ORDER BY RAND() LIMIT 1;")
    myresult = mycursor.fetchone()
    await ctx.send(myresult)

@client.command(aliases=['Show_mark1', 'Show_Mark1', 'SHOW_MARK1'],help='show_mark1 (returns only one random 1marks questions)')
async def show_mark1(ctx):
    mycursor.execute("SELECT questions FROM Question1Marks ORDER BY RAND() LIMIT 1;")
    myresult = mycursor.fetchone()
    await ctx.send(myresult)


@client.command(aliases=['Showall_mark5', 'Showall_Mark5', 'SHOWALL_MARK5'],help='showall_mark5 (returns all 5marks questions)')
async def showall_mark5(ctx):
    mycursor.execute("SELECT questions FROM Question5Marks;")
    myresult = mycursor.fetchall()
    for x in myresult:
        await ctx.send(myresult)


@client.command(aliases=['Showall_mark4', 'Showall_Mark4', 'SHOWALL_MARK4'],help='showall_mark4 (returns all 4marks questions)')
async def showall_mark4(ctx):
    mycursor.execute("SELECT questions FROM Question4Marks;")
    myresult = mycursor.fetchall()
    await ctx.send(myresult)

@client.command(aliases=['Showall_mark3', 'Showall_Mark3', 'SHOWALL_MARK3'],help='showall_mark3 (returns all 3marks questions)')
async def showall_mark3(ctx):
    mycursor.execute("SELECT questions FROM Question3Marks;")
    myresult = mycursor.fetchall()
    await ctx.send(myresult)

@client.command(aliases=['Showall_mark2', 'Showall_Mark2', 'SHOWALL_MARK2'],help='showall_mark2 (returns all 2marks questions)')
async def showall_mark2(ctx):
    mycursor.execute("SELECT questions FROM Question2Marks;")
    myresult = mycursor.fetchall()
    await ctx.send(myresult)

@client.command(aliases=['Showall_mark1', 'Showall_Mark1', 'SHOWALL_MARK1'],help='showall_mark1 (returns all 1marks questions)')
async def showall_mark1(ctx):
    mycursor.execute("SELECT questions FROM Question1Marks;")
    myresult = mycursor.fetchall()
    await ctx.send(myresult)

@client.command(aliases=['Filtersubject'],help='filtersubject <subject_name>')
async def filtersubject(ctx,*,data):
    sql = "SELECT questions FROM Question5Marks WHERE Subject = (%s);"
    val = [data]
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        await ctx.send(myresult)
    sql = "SELECT questions FROM Question4Marks WHERE Subject = (%s);"
    val = [data]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        await ctx.send(myresult)
    sql = "SELECT questions FROM Question3Marks WHERE Subject = (%s);"
    val = [data]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        await ctx.send(myresult)
    sql = "SELECT questions FROM Question2Marks WHERE Subject = (%s);"
    val = [data]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        await ctx.send(myresult)
    sql = "SELECT questions FROM Question1Marks WHERE Subject = (%s);"
    val = [data]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        await ctx.send(myresult)

@client.command(aliases=['Filtertopic'],help='filtertopic <topic_name>')
async def filtertopic(ctx,*,data):
    sql = "SELECT questions FROM Question5Marks WHERE Topic = (%s);"
    val = [data]
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        await ctx.send(myresult)
    sql = "SELECT questions FROM Question4Marks WHERE Topic = (%s);"
    val = [data]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        await ctx.send(myresult)
    sql = "SELECT questions FROM Question3Marks WHERE Topic = (%s);"
    val = [data]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        await ctx.send(myresult)
    sql = "SELECT questions FROM Question2Marks WHERE Topic = (%s);"
    val = [data]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        await ctx.send(myresult)
    sql = "SELECT questions FROM Question1Marks WHERE Topic = (%s);"
    val = [data]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        await ctx.send(myresult)

@client.command(aliases=['FilterChapter'],help='filterchapter <chapter_name>')
async def filterChapter(ctx,*,data):
    sql = "SELECT questions FROM Question5Marks WHERE Chapter = (%s);"
    val = [data]
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        await ctx.send(myresult)
    sql = "SELECT questions FROM Question4Marks WHERE Chapter = (%s);"
    val = [data]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        await ctx.send(myresult)
    sql = "SELECT questions FROM Question3Marks WHERE Chapter = (%s);"
    val = [data]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        await ctx.send(myresult)
    sql = "SELECT questions FROM Question2Marks WHERE Chapter = (%s);"
    val = [data]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        await ctx.send(myresult)
    sql = "SELECT questions FROM Question1Marks WHERE Chapter = (%s);"
    val = [data]
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        await ctx.send(myresult)


@client.command(help='removechannel <channelid> Admins only')
@commands.has_role("Admin")
async def removechannel(ctx, channel: discord.TextChannel):
    await channel.delete()
    await ctx.send("```Successfully deleted the channel!```")

@client.command(aliases=['Clear'],help='clear(int) Admins only')
@commands.has_permissions(manage_guild = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit = amount)

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("Invalid Command")
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Incomplete Command")
        await ctx.message.delete()

client.run(TOKEN)
