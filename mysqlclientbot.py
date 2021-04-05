from discord.ext import commands
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="14147714", database="vinamradb")

mycursor = mydb.cursor()

TOKEN = "ODI4MjUzMzQ4MzE0MzQ5NTY4.YGm5Cg.deGSFktLDr28Mdt4Ng7tMXKobHQ"
client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print("bot is ready to takeoff")



@client.command(aliases=['mysqledit'],help = "$Mysqledit <sql query> only applicable for non-returnable queries")
async def Mysqledit(ctx, *, data):
    sql = data
    mycursor.execute(sql)
    mydb.commit()
    await ctx.send("Commit succesfull")

@client.command(aliases=['mysql'],help = "$Mysqledit <sql query>")
async def Mysql(ctx, *, data):
    sql = data
    mycursor.execute(sql)
    try:
        myresult = mycursor.fetchall()
    except:
        myresult = mycursor.fetchone()
    await ctx.send("Commit succesfull")
    await ctx.send(myresult)


client.run(TOKEN)