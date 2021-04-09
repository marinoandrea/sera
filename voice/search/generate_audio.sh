#!/bin/sh

echo generating EN audio...
# english
gtts-cli 'Welcome to Sera! For English audio press 1, for French audio press 2.' --output en/audio/welcome.mp3
gtts-cli 'What type of seed do you want to buy? For Fonio press 1, for Gombo press 2, for Mais press 3, for Sorgho press 4.' --output en/audio/category.mp3
gtts-cli "What type of Fonio do you want to buy? For Pon de Bore press 1, For Niatia press 2, For Banco Konkountre press 3, For any Other type press 4, To go back, press the asterisk." --output en/audio/subcategory_fonio.mp3;
gtts-cli "What type of Gombo do you want to buy? For Keleya press 1, For Sabalibougou press 2, For Gansourouni press 3, For any Other type press 4, To go back, press the asterisk." --output en/audio/subcategory_gombo.mp3;
gtts-cli "What type of Mais do you want to buy? For Sotubaka press 1, For Nieleni press 2, For Dembaniouma press 3, For any Other type press 4, To go back, press the asterisk." --output en/audio/subcategory_mais.mp3;
gtts-cli "What type of Sorgho do you want to buy? For Toroba press 1, For Bobodje press 2, For Tieblen press 3, For any Other type press 4, To go back, press the asterisk." --output en/audio/subcategory_sorgho.mp3;
gtts-cli "How many kilos do you want to buy? Please give the minimum amount and then press the HashTag." --output en/audio/quantity_min.mp3;
gtts-cli "How many kilos do you want to buy? Please give the maximum amount and then press the HashTag." --output en/audio/quantity_max.mp3;
gtts-cli "You made the following search. Category:" --output en/audio/results_category.mp3;
gtts-cli "Subcategory:" --output en/audio/results_subcategory.mp3;
gtts-cli "Minimum quantity:" --output en/audio/results_quantity_min.mp3;
gtts-cli "Maximum quantity:" --output en/audio/results_quantity_max.mp3;
gtts-cli "To listen the results of your search, press 1. To make a new search, press the Asterisk." --output en/audio/review_instructions.mp3;
# - misc
gtts-cli "kilos" --output en/audio/kilos.mp3;
gtts-cli "Something went wrong, try again later." --output en/audio/error.mp3;
# - mock data
gtts-cli "There is one active offering fitting your search criteria." --output en/audio/mock_result_1.mp3;
gtts-cli "kilos of" --output en/audio/mock_result_2.mp3;
gtts-cli "for the price of 500 Francs." --output en/audio/mock_result_3.mp3;
echo OK

echo generating FR audio...
# french
gtts-cli "Bienvenue à Sera! Pour l'audio anglais, appuyez sur 1, pour l'audio français appuyez sur 2." --lang fr --output fr/audio/welcome.mp3
gtts-cli "Quel type de semences voulez-vous acheter ? Pour Fonio appuyez sur 1, pour Gombo appuyez sur 2, pour Mais appuyez sur 3, pour Sorgho appuyez sur 4." --lang fr --output fr/audio/category.mp3 
gtts-cli "Quel type de Fonio voulez-vous acheter ? Pour Pon de Bore appuyez sur 1, Pour Niatia appuyez sur 2, Pour Banco Konkountre pressez 3, Pour tout autre type, appuyez sur 4, Pour revenir en arrière, appuyez sur l'astérisque." --lang fr --output fr/audio/subcategory_fonio.mp3;
gtts-cli "Quel type de Gombo voulez-vous acheter ? Pour Keleya appuyez sur 1, Pour Sabalibougou appuyez sur 2, Pour Gansourouni pressez 3, Pour tout autre type, appuyez sur 4, Pour revenir en arrière, appuyez sur l'astérisque." --lang fr --output fr/audio/subcategory_gombo.mp3;
gtts-cli "Quel type de Mais voulez-vous acheter ? Pour Sotubaka appuyez sur 1, Pour Nieleni appuyez sur 2, Pour Dembaniouma pressez 3, Pour tout autre type, appuyez sur 4, Pour revenir en arrière, appuyez sur l'astérisque." --lang fr --output fr/audio/subcategory_mais.mp3;
gtts-cli "Quel type de Sorgho voulez-vous acheter ? Pour Toroba appuyez sur 1, Pour Bobodje appuyez sur 2, Pour Tieblen pressez 3, Pour tout autre type, appuyez sur 4, Pour revenir en arrière, appuyez sur l'astérisque." --lang fr --output fr/audio/subcategory_sorgho.mp3;
gtts-cli "Combien de kilos voulez-vous acheter? Veuillez indiquer le montant minimum, puis appuyez sur le HashTag." --lang fr --output fr/audio/quantity_min.mp3;
gtts-cli "Combien de kilos voulez-vous acheter? Veuillez indiquer le montant maximum, puis appuyez sur le HashTag." --lang fr --output fr/audio/quantity_max.mp3;
gtts-cli "Vous avez effectué la recherche suivante. Catégorie:" --lang fr --output fr/audio/results_category.mp3;
gtts-cli "Sous-Catégorie:" --lang fr --output fr/audio/results_subcategory.mp3;
gtts-cli "Quantité minimum:" --lang fr --output fr/audio/results_quantity_min.mp3;
gtts-cli "Quantité maximum:" --lang fr --output fr/audio/results_quantity_max.mp3;
gtts-cli "Pour écouter les résultats de votre recherche, appuyez sur 1. Pour effectuer une nouvelle recherche, appuyez sur l'astérisque" --output fr/audio/review_instructions.mp3;
# - misc
gtts-cli "kilos" --lang fr --output fr/audio/kilos.mp3;
gtts-cli "Quelque chose s'est mal passé, réessayez plus tard." --lang fr --output fr/audio/error.mp3;
# - mock data
gtts-cli "Il existe une offre active correspondant à vos critères de recherche." --lang fr --output fr/audio/mock_result_1.mp3;
gtts-cli "kilos de" --lang fr --output fr/audio/mock_result_2.mp3;
gtts-cli "pour le prix de 500 francs." --lang fr --output fr/audio/mock_result_3.mp3;
echo OK

echo processing audio...
files=$(find . -type f -name "*.mp3")
for f in $files
do
    sox $f -b 16 -c 1 -e signed-integer "./$(echo $f | cut -d. -f2).wav" rate 8k
    rm $f
done
echo OK