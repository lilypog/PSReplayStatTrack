import json
pokemonList = []

def starts_poke_p1(w):
        return w.startswith("|poke|p1")
def starts_poke_p2(w):
        return w.startswith("|poke|p2")

with open("C:\\Users\\camtk\\OneDrive\\Desktop\\PSStatTrack\\PSReplayStatTrack\\lilyvmatt.json", "r") as file:
        data = json.load(file)
        pkmnText = json.dumps(data["log"], ensure_ascii=False)
        lines = pkmnText.split("\\n")
        pokemonListp1 = list(filter(starts_poke_p1, lines))
        pokemonListp1 = str(pokemonListp1)
        pokemonListp1 = pokemonListp1.replace("|poke|p1|", "")
        pokemonListp1 = pokemonListp1.replace("|item", "")
        pokemonListp1 = pokemonListp1.replace(", F", "")
        pokemonListp1 = pokemonListp1.replace(", M", "")
        pokemonListp1 = pokemonListp1.replace("[", "")
        pokemonListp1 = pokemonListp1.replace("]", "")
        pokemonListp1 = pokemonListp1.replace("'", "")
        pokemonListp1 = pokemonListp1.split(", ")

        pokemonListp2 = list(filter(starts_poke_p2, lines))
        pokemonListp2 = str(pokemonListp2)
        pokemonListp2 = pokemonListp2.replace("|poke|p2|", "")
        pokemonListp2 = pokemonListp2.replace("|item", "")
        pokemonListp2 = pokemonListp2.replace(", F", "")
        pokemonListp2 = pokemonListp2.replace(", M", "")
        pokemonListp2 = pokemonListp2.replace("[", "")
        pokemonListp2 = pokemonListp2.replace("]", "")
        pokemonListp2 = pokemonListp2.replace("'", "")
        pokemonListp2 = pokemonListp2.split(", ")

print(pokemonListp1)
print(pokemonListp2)

# Separate pokemon into elements