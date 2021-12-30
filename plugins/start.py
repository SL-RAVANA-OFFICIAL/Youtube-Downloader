
from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Updates Channel", url="https://t.me/slravanaofficial")
      ],
      [ 
        InlineKeyboardButton(
            "Support Group", url="https://t.me/slravanaofficial")]
    ])
    welcomed = f"<b> Hey {message.from_user.first_name} , \n\nමම Youtube Video Downloader Bot මට Youtube Videos & Audios Download කල හැක යූටුයුබ් එක හරහා. \n\nBot BY SL RAVANA TEAM \n\nCreated By @MR_RAVANA_OFFICIAL </b>"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagatio
