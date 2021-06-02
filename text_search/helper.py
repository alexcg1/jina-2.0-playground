from jina import Flow, Document, DocumentArray, Executor, requests


class Capitalizer(Executor):
    """Capitalizer executor class """

    @requests
    def capitalize(self, docs, *args, **kwargs):
        for doc in docs:
            doc.text = doc.text.upper()


superman = Document(
    content="""
Superman, born Kal-El and legally named Clark Joseph Kent, is the last son of Krypton, sent as the dying planet's last hope to Earth, where he grew to become its protector. Though he was apparently killed shortly after the Darkseid War, his essence merged with the New Earth Superman in Rebirth, creating a new, merged timeline for Superman.
""",
    tags={
        "secret_identity": "Clark Kent",
        "home": "Metropolis",
        "powers": ["Flight", "X-ray vision", "Strength"],
        "name": "Superman",
    },
)

batman = Document(
    content="""
Batman is the super-hero protector of Gotham City, a man dressed like a bat who fights against evil and strikes terror into the hearts of criminals everywhere. In his secret identity, he assumes the alias of Bruce Wayne, billionaire industrialist and notorious playboy; though "Bruce Wayne" is technically his real name, this Bruce Wayne is a disguise--that of the man he would have been had his parents not been murdered before his eyes when he was no more than a mere boy. 
""",
    tags={
        "secret_identity": "Bruce Wayne",
        "home": "Gotham",
        "powers": ["Money"],
        "name": "Batman",
    },
)

spiderman = Document(
    content="""
Peter Benjamin Parker lost his parents, Richard and Mary Parker, at a young age. Orphaned as a toddler, he had to live with his Uncle Ben and Aunt May. During a science exhibition, he was bitten by a Radioactive Spider, granting him his powers. He decided to use these powers for his own selfish gain, until his Uncle Ben died at the hands of a Burglar he could've stopped. It was at that point that he learned "With great power, there must also come great responsibility", and decided to live up to his uncle's mantra and use his powers as a force for good as Spider-Man. 
    """,
    tags={
        "secret_identity": "Peter Parker",
        "home": "New York",
        "powers": ["Spider sense", "Webbing"],
        "name": "Spider-Man",
    },
)

captain_america = Document(
    content="""
During the dark days of the early 1940's, a covert U.S. Military experiment turned Steve Rogers into America's first Super-Soldier, Captain America. Throughout the war, Cap and his partner, Bucky fought alongside infantry and with a group of heroes known as the Invaders. In the closing months of World War II, Captain America and Bucky were both presumed dead in an explosion. Decades later, Captain America was found trapped in ice and revived in the modern world. Captain America would then later go on to be one of the most important members of the Avengers as well as a leader of the team. 
    """,
    tags={
        "secret_identity": "Steve Rogers",
        "home": "New York",
        "powers": ["Super strength", "Endurance"],
        "name": "Captain America",
    },
)


dc_comics = Document(chunks=[batman, superman])
marvel_comics = Document(chunks=[spiderman, captain_america])


docs = DocumentArray([dc_comics, marvel_comics])
