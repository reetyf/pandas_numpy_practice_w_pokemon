import dmg
import pokemon

Charizard = pokemon.Pokemon("Charizard", "fire", "flying", 84, 78, 109, 85, 100)
Venusaur = pokemon.Pokemon("Venusaur", "grass", "poison", 82, 83, 100, 100, 80)
(damage, critflag, superEff, doesntEff, notVeryEff,missed) = dmg.attack(False, "fire", Charizard.type1, Charizard.type2, Venusaur.type1, Venusaur.type2, 110, 85, Charizard.attack, Venusaur.defense, Charizard.spattack, Venusaur.spdef)
dmg.battleString(Charizard, Venusaur, "Fire Blast" , damage, critflag, superEff, doesntEff, notVeryEff ,missed)