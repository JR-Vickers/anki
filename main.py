import genanki

windows_directories = [
    ("C:\\", "Root Directory: This is the top-most directory of the file system."),
    ("Windows\\", "Core directory where the Windows operating system resides."),
    ("Windows\\System32\\", "Contains core system files and libraries."),
    ("Windows\\SysWOW64\\", "Contains 32-bit system files on a 64-bit Windows installation."),
    ("Windows\\Temp\\", "Temporary files used by the system and other software."),
    ("Program Files\\", "Where most 64-bit applications are installed by default."),
    ("Program Files (x86)\\", "On a 64-bit Windows system, 32-bit applications are typically installed here."),
    ("Users\\", "Contains personal directories for each user on the system."),
    ("Users\\Desktop\\", "Contains files and shortcuts present on the user’s desktop."),
    ("Users\\Documents\\", "Default location for storing personal documents."),
    ("Users\\Downloads\\", "Default directory for files downloaded from the internet."),
    ("Users\\Pictures\\", "Default directories for personal media files."),
    ("Users\\Music\\", "Default directories for personal media files."),
    ("Users\\Videos\\", "Default directories for personal media files."),
    ("Users\\AppData\\", "Contains application-specific data for each user, including settings, cache, etc."),
    ("Users\\AppData\\Local\\", "Contains data that is not synced between computers when using a roaming profile."),
    ("Users\\AppData\\Roaming\\", "Contains data that can roam with a user's profile across different computers."),
    ("Users\\AppData\\LocalLow\\", "Contains low integrity data (often used by Internet Explorer)."),
    ("ProgramData\\", "Contains application and system data that isn't specific to a user."),
    ("Recovery\\", "Hidden directory used for the system's recovery tools."),
    ("$Recycle.Bin\\", "System’s trash/recycling bin."),
    ("Boot\\", "Contains files needed to boot the Windows operating system."),
    ("PerfLogs\\", "Stores performance and reliability logs."),
    ("System Volume Information\\", "Hidden directory that stores system information and Restore Point data.")
]

# Define Anki note model
model_id = 1607392319
model = genanki.Model(
    model_id,
    'Windows filesystem folders',
    fields=[
        {'name': 'Directory'},
        {'name': 'Description'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Directory}}',
            'afmt': '{{Description}}',
        },
        {
            'name': 'Card 2',
            'qfmt': '{{Description}}',
            'afmt': '{{Directory}}',
        },
    ])

# Generate Anki cards and add them to a deck
deck_id = 2059400110
deck = genanki.Deck(deck_id, 'Linux Filesystem')

for dir_name, description in windows_directories:
    note = genanki.Note(model=model, fields=[dir_name, description])
    deck.add_note(note)

# Save the deck to an Anki package (*.apkg) file
genanki.Package(deck).write_to_file('windows_filesystem.apkg')