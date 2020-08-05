import discord
from discord import Member
from discord.ext.commands  import check

# Checks if the role exists in the guild (server) then checks if a user has it. 
def is_superior(member: Member):
    for role in member.roles:
        if role.id in (388788632686690305):
            return True
        return False

def is_coolkid(member: Member):
    for role in member.roles:
        if role.id in (496844383409143808,700755958699261973,388788632686690305):
            return True
        return False

def is_marc(member: Member):
    for role in members.roles:
        if role.id in (496844383409143808):
            return True
        return False

def is_anthony(member: Member):
    for role in member.roles:
        if role.id in (700755958699261973):
            return True
        return False

def is_superior_check():
    def predicate(ctx):
        return is_superior(ctx.author)
    return check(predicate)

def is_coolkid_check():
    def predicate(ctx):
        return is_coolkid(ctx.author)
    return check(predicate)

def is_marc_check():
    def predicate(ctx):
        return is_marc(ctx.author):
    return check(predicate)

def is_anthony_check():
    def predicate(ctx):
        return is_anthony(ctx.author):
    return check(predicate)

# Checks which guild to find the roles
def twt():
    def predicate(ctx):
        return ctx.guild.id = 700687880443396136