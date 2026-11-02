{
    "name": "MCP for Claude & ChatGPT",
    "version": "20.0.1.1.0",
    "category": "Productivity",
    "summary": (
        "Tuqui is a hosted MCP server for Odoo: connect your database at tuqui.com and ask "
        "Claude, ChatGPT, Cursor or any MCP client about your sales, stock or invoices, with "
        "answers from your real data. The connection is made at tuqui.com and needs no code in "
        "Odoo; works on Odoo Online, Odoo.sh and On-Premise. Standard OAuth 2.0, within each "
        "user's permissions."
    ),
    "author": "Tuqui-AI",
    "website": "https://tuqui.com",
    "license": "LGPL-3",
    "images": ["static/description/portada.png"],
    "depends": ["base"],
    "data": [
        "data/tuqui_mcp_data.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
