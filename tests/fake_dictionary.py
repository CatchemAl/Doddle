from doddle.words import Dictionary, WordSeries


def load_test_dictionary(size: int = 5) -> Dictionary:

    common = {
        "ADMIN",
        "ALIEN",
        "ANGLE",
        "ARSON",
        "ARROW",
        "BACON",
        "BEFIT",
        "BIRTH",
        "BLUFF",
        "BRAKE",
        "BRUSH",
        "CADDY",
        "CHAIN",
        "CHILD",
        "CHORD",
        "CLING",
        "CORER",
        "CREEK",
        "CUMIN",
        "DECRY",
        "DITCH",
        "DRESS",
        "DWELT",
        "EMBER",
        "EVERY",
        "FEIGN",
        "FINER",
        "FLOUR",
        "FLACK",
        "FLAME",
        "FRAME",
        "FUNKY",
        "GAFFE",
        "GLAND",
        "GRACE",
        "GROUP",
        "HARDY",
        "HIPPY",
        "HYDRO",
        "INTRO",
        "KAYAK",
        "LATCH",
        "LIGHT",
        "LIKEN",
        "LOYAL",
        "MANGA",
        "MERGE",
        "MONTH",
        "MOUNT",
        "MUSKY",
        "NOOSE",
        "NOTCH",
        "OPIUM",
        "PAPER",
        "PETAL",
        "PLANT",
        "PRANK",
        "PULPY",
        "QUILT",
        "RAISE",
        "REACT",
        "RETRO",
        "ROOMY",
        "SALVO",
        "SCOPE",
        "SHAFT",
        "SHOAL",
        "SIXTH",
        "SLOPE",
        "SNACK",
        "SNAKE",
        "SNEAK",
        "SPARK",
        "SPOOL",
        "STASH",
        "STICK",
        "STOLE",
        "STORE",
        "SURLY",
        "TACIT",
        "TEPEE",
        "TIBIA",
        "TOWER",
        "TOXIC",
        "TRUER",
        "UNCLE",
        "VALET",
        "VIVID",
        "WEIRD",
        "WINCE",
        "WRITE",
    }

    uncommon = {
        "ADMIT",
        "ALIGN",
        "ANGRY",
        "ARTSY",
        "BADGE",
        "BEGAN",
        "BILLY",
        "BISON",
        "BLUDY",
        "BLUNT",
        "BRAND",
        "BRUTE",
        "CADET",
        "CHAIR",
        "CHORE",
        "CLINK",
        "CORNY",
        "CREEP",
        "CURIO",
        "DEFER",
        "DITTO",
        "DRIED",
        "DYING",
        "EMCEE",
        "EVICT",
        "FANGO",
        "FELLA",
        "FILLY",
        "FIRST",
        "FLOUT",
        "FRANK",
        "GAILY",
        "GLARE",
        "GRADE",
        "GROUT",
        "HAREM",
        "HITCH",
        "HYENA",
        "IONIC",
        "KEBAB",
        "LATER",
        "LILAC",
        "LUCID",
        "MANGE",
        "MERIT",
        "MOODY",
        "MULCH",
        "MUSTY",
        "NORTH",
        "OPTIC",
        "PARER",
        "PETTY",
        "PLATE",
        "PRAWN",
        "PULSE",
        "QUIRK",
        "READY",
        "RETRY",
        "ROOST",
        "SANDY",
        "SCORE",
        "SHAKE",
        "SHOCK",
        "SIXTY",
        "SLOSH",
        "SNEER",
        "SPASM",
        "SPOON",
        "STATE",
        "STINK",
        "STORK",
        "SUSHI",
        "TACKY",
        "TEPID",
        "TIDAL",
        "TOXIN",
        "TRULY",
        "UNCUT",
        "VALID",
        "VIXEN",
        "WELCH",
        "WINCH",
        "WRONG",
        "ZEBRA",
    }

    common_words = WordSeries(common)
    all_words = WordSeries(common.union(uncommon))
    return Dictionary(all_words, common_words)
