print("Welcome to the Manga Reader Recommender!")
print("Answer a few questions to find new things to read.")
print("What genre do you like?")
print("1. action")
print("2. fantasy")
print("3. horror")
print("4. sci-fi")

genre = input("Enter your genre choice (1/2/3/4): ")
duration = input("Choose the length you wanted: short, medium, long: ")
year = eval(input("Which decade? (2000, 2010): "))

print("Here are some recommendations based on your preferences!")
if genre == "1" and duration == "short":
	if year == 2000:
		print("\n Sandland (2000)\n", "Anne Freaks (2000–2002)\n", "Batman: Child of Dreams (2000)")
	if year == 2010:
		print("\n Fire Punch (2016)\n", "Black Torch (2016–2018)\n", "Red Raven (2010)")
if genre == "1" and duration == "medium":
	if year == 2000:
		print("\n Psyren (2007–2010)\n", "Black Cat (2000–2004)\n", "Battle Royal (2000-2005)")
	if year == 2010:
		print("\n Akame ga Kill! (2010–2016)\n", "Jujutsu Kaisen (2018–present)\n", "Tokyo Revengers(2017–2022)")
if genre == "1" and duration == "long":
	if year == 2000:
		print("\n Naruto (1999–2014)\n", "Bleach (2001–2016)\n", "Eyeshield 21 (2002–2009)")
	if year == 2010:
		print("\n My Hero Academia (2014–present)\n", "Black Clover (2015–present)\n", "World Trigger (2013–present)")
if genre == "2" and duration == "short":
	if year == 2000:
		print("\n Jihai (2004–2006)\n", "Dragon Eye (2005–2008)\n", "Kazan (2000–2001)")
	if year == 2010:
		print("\n Kiba no Tabishounin (2014–2016)\n", "Shinazu no Ryouken (2017–2019)\n", "Kuro no Shoukanshi (Black Summoner) (2014–2019)")
if genre == "2" and duration == "medium":
	if year == 2000:
		print("\n Tegami Bachi (Letter Bee) (2006–2015)\n", "Magico (2011–2012)\n", "Kekkaishi (2003–2011)")
	if year == 2010:
		print("\n Grimgar: Ashes and Illusions (2015–2020)\n", "The Ancient Magus’ Bride (2013–present)\n", "Re:Monster (2014–present)")
if genre == "2" and duration == "long":
	if year == 2000:
		print("\n Tales of the Abyss (2005–2010s)\n", "Zatch Bell! (Konjiki no Gash!!)  (2001–2007)\n", "MÄR Omega (2006–2007)")
	if year == 2010:
		print("\n Twin Star Exorcists (2013–2022)\n", "Jobless Reincarnation (2014–present)\n", "Yamada Tarou Monogatari: Reboot (2010–2018)")
if genre == "3" and duration == "short":
	if year == 2000:
		print("\n Fuan no Tane (2004–2005)\n", "Me wo Mite Hanase (2000s)\n", "Layers of Fear (2000s)")
	if year == 2010:
		print("\n Sleeping Dead (2010s)\n", "Sono Mori no Hanashi (2016)\n", "Zansatsu! Ponytail (2016)")
if genre == "3" and duration == "medium":
	if year == 2000:
		print("\n Shiki (2007–2011)\n", "Kakugo no Susume (2000–2004)\n", "Togari (2000–2002)")
	if year == 2010:
		print("\n MADK (2017–2020)\n", "Children (2017–2019)\n", "Heartless (2016–2018)")
if genre == "3" and duration == "long":
	if year == 2000:
		print("\n Detective School Q (2001–2005)\n", "Kyoufu Gakuen (2000s)\n", "Yami no Koe (2000s)")
	if year == 2010:
		print("\n Devilman Grimoire (2012–2014)\n", "Ajin: Demi-Human (2012–2021)\n", "Killing Morph (2017–present)")
if genre == "4" and duration == "short":
	if year == 2000:
		print("\n Blue Heaven (2002–2003)\n", "Reset (2005–2006)\n", "Present for Me (2008)")
	if year == 2010:
		print("\n Mujirushi: The Sign of Dreams (2017–2018)\n", "Origin (2016–2019)\n", "Atom: The Beginning (2014–2019)")
if genre == "4" and duration == "medium":
	if year == 2000:
		print("\n King of Thorn (2002–2005)\n", "Blame! Academy and So On (2000s)\n", "Planetes (2000–2004)")
	if year == 2010:
		print("\n Dimension W (2011–2019)\n", "Terra Formars (2011–2020)\n", "World's End Harem (2016–2021)")
if genre == "4" and duration == "long":
	if year == 2000:
		print("\n Tsubasa: Reservoir Chronicle (2003–2009)\n", "Linebarrels of Iron (2005–2014)\n", "Zetman (2002–2014)")
	if year == 2010:
		print("\n Astra Lost in Space (2016–2018)\n", "Boku no Hero Academia: Vigilantes (2016–2022)\n", "Blue Hole: The Deep Sea (2010s)")
else:
	print("Invalid input. Please restart again.")
