#!/bin/sh

echo generating EN audio...
# english
gtts-cli 'Welcome to Sera! For English audio press 1, for French audio press 2.' --output en/audio/welcome.mp3
gtts-cli 'What type of seed do you want to sell? For Fonio press 1, for Rice press 2, for Mais press 3, for Sorghum press 4.' --output en/audio/category.mp3
gtts-cli "What type of Millet do you want to sell? For Pon de Bore press 1, For Niatia press 2, For Banco Konkountre press 3, For any Other type press 4, To go back, press the asterisk." --output en/audio/subcategory_fonio.mp3;
gtts-cli "What type of Rice do you want to sell? For Gambiaka press 1, For Shwetassoke press 2, For Nerica press 3, For any Other type press 4, To go back, press the asterisk." --output en/audio/subcategory_rice.mp3;
gtts-cli "What type of Mais do you want to sell? For Sotubaka press 1, For Nieleni press 2, For Dembaniouma press 3, For any Other type press 4, To go back, press the asterisk." --output en/audio/subcategory_mais.mp3;
gtts-cli "What type of Sorghum do you want to sell? For Toroba press 1, For Bobodje press 2, For Tieblen press 3, For any Other type press 4, To go back, press the asterisk." --output en/audio/subcategory_sorgho.mp3;
gtts-cli "How many kilos do you want to sell? Insert the amount and then press the HashTag." --output en/audio/quantity.mp3;
gtts-cli "At what price do you want to sell? Insert the price and then press the HashTag." --output en/audio/price.mp3;
gtts-cli "You have selected the category:" --output en/audio/review_category.mp3;
gtts-cli "You have selected the subcategory:" --output en/audio/review_subcategory.mp3;
gtts-cli "You have selected the quantity:" --output en/audio/review_quantity.mp3;
gtts-cli "You have selected the price:" --output en/audio/review_price.mp3;
gtts-cli "To confirm press 1, To go back press the Asterisk." --output en/audio/review_instructions.mp3;
gtts-cli "Your announcement has been uploaded! Thank your for using Sera!" --output en/audio/review_sent.mp3;
# - misc
gtts-cli "kilos" --output en/audio/kilos.mp3;
gtts-cli "Something went wrong, try again later." --output en/audio/error.mp3;
echo OK

echo generating FR audio...
# french
gtts-cli "Bienvenue à Sera! Pour l'audio anglais, appuyez sur 1, pour l'audio français appuyez sur 2." --lang fr --output fr/audio/welcome.mp3
gtts-cli "Quel type de semences voulez-vous vendre ? Pour Fonio appuyez sur 1, pour Riz appuyez sur 2, pour Mais appuyez sur 3, pour Sorgho appuyez sur 4." --lang fr --output fr/audio/category.mp3 
gtts-cli "Quel type de Fonio voulez-vous vendre ? Pour Pon de Bore appuyez sur 1, Pour Niatia appuyez sur 2, Pour Banco Konkountre pressez 3, Pour tout autre type, appuyez sur 4, Pour revenir en arrière, appuyez sur l'astérisque." --lang fr --output fr/audio/subcategory_fonio.mp3;
gtts-cli "Quel type de Riz voulez-vous vendre ? Pour Gambiaka appuyez sur 1, Pour Shwetassoke appuyez sur 2, Pour Nerica pressez 3, Pour tout autre type, appuyez sur 4, Pour revenir en arrière, appuyez sur l'astérisque." --lang fr --output fr/audio/subcategory_rice.mp3;
gtts-cli "Quel type de Mais voulez-vous vendre ? Pour Sotubaka appuyez sur 1, Pour Nieleni appuyez sur 2, Pour Dembaniouma pressez 3, Pour tout autre type, appuyez sur 4, Pour revenir en arrière, appuyez sur l'astérisque." --lang fr --output fr/audio/subcategory_mais.mp3;
gtts-cli "Quel type de Sorgho voulez-vous vendre ? Pour Toroba appuyez sur 1, Pour Bobodje appuyez sur 2, Pour Tieblen pressez 3, Pour tout autre type, appuyez sur 4, Pour revenir en arrière, appuyez sur l'astérisque." --lang fr --output fr/audio/subcategory_sorgho.mp3;
gtts-cli "Combien de kilos voulez-vous vendre? Insérez le montant, puis appuyez sur le HashTag.." --lang fr --output fr/audio/quantity.mp3;
gtts-cli "À quel prix voulez-vous vendre ? Insérez le prix, puis appuyez sur le HashTag." --lang fr --output fr/audio/price.mp3;
gtts-cli "Vous avez sélectionné la catégorie:" --lang fr --output fr/audio/review_category.mp3;
gtts-cli "Vous avez sélectionné type:" --lang fr --output fr/audio/review_subcategory.mp3;
gtts-cli "Vous avez sélectionné la quantité:" --lang fr --output fr/audio/review_quantity.mp3;
gtts-cli "Vous avez sélectionné le prix:" --lang fr --output fr/audio/review_price.mp3;
gtts-cli "Pour confirmer, appuyez sur 1, Pour revenir en arrière, appuyez sur l'astérisque." --lang fr --output fr/audio/review_instructions.mp3;
gtts-cli "Votre annonce a été téléchargée! Merci d'avoir utilisé Sera!" --lang fr --output fr/audio/review_sent.mp3;
# - misc
gtts-cli "kilos" --lang fr --output fr/audio/kilos.mp3;
gtts-cli "Quelque chose s'est mal passé, réessayez plus tard." --lang fr --output fr/audio/error.mp3;
echo OK

echo processing audio...
files=$(find . -type f -name "*.mp3")
for f in $files
do
    sox $f -b 16 -c 1 -e signed-integer "./$(echo $f | cut -d. -f2).wav" rate 8k
    rm $f
done
echo OK
