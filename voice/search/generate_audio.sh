#!/bin/sh

echo generating EN audio...
# english
gtts-cli 'Welcome to Sera! For English audio press 1, for French audio press 2.' --output audio/en/welcome.wav
gtts-cli "What type of Fonio do you want to buy? For Pon de Bore press 1, For Niatia press 2, For Banco Konkountre press 3, For any Other type press 4, To go back, press the asterisk." --output audio/en/subcategory_fonio.wav;
gtts-cli "What type of Gombo do you want to buy? For Keleya press 1, For Sabalibougou press 2, For Gansourouni press 3, For any Other type press 4, To go back, press the asterisk." --output audio/en/subcategory_gombo.wav;
gtts-cli "What type of Mais do you want to buy? For Sotubaka press 1, For Nieleni press 2, For Dembaniouma press 3, For any Other type press 4, To go back, press the asterisk." --output audio/en/subcategory_mais.wav;
gtts-cli "What type of Sorgho do you want to buy? For Toroba press 1, For Bobodje press 2, For Tieblen press 3, For any Other type press 4, To go back, press the asterisk." --output audio/en/subcategory_sorgho.wav;
gtts-cli "How many kilos do you want to buy? Please give the minimum amount and then press the HashTag." --output audio/en/quantity_min.wav;
gtts-cli "How many kilos do you want to buy? Please give the maximum amount and then press the HashTag." --output audio/en/quantity_max.wav;
gtts-cli "You made the following search. Category:" --output audio/en/results_category.wav;
gtts-cli "Subcategory:" --output audio/en/results_subcategory.wav;
gtts-cli "Minimum quantity:" --output audio/en/results_quantity_min.wav;
gtts-cli "Maximum quantity:" --output audio/en/results_quantity_max.wav;
gtts-cli "To listen the results of your search, press 1. To make a new search, press the Asterisk." --output audio/en/review_instructions.wav;
# - misc
gtts-cli "kilos" --output audio/en/kilos.wav;
gtts-cli "Something went wrong, try again later." --output audio/en/error.wav;
# - mock data
gtts-cli "There is one active offering fitting your search criteria." --output audio/en/mock_result_1.wav;
gtts-cli "kilos of" --output audio/en/mock_result_2.wav;
gtts-cli "for the price of 500 Francs." --output audio/en/mock_result_3.wav;
echo OK

echo generating FR audio...
# french
gtts-cli "Bienvenue à Sera! Pour l'audio anglais, appuyez sur 1, pour l'audio français appuyez sur 2." --lang fr --output audio/fr/welcome.wav
gtts-cli "Quel type de Fonio voulez-vous acheter ? Pour Pon de Bore appuyez sur 1, Pour Niatia appuyez sur 2, Pour Banco Konkountre pressez 3, Pour tout autre type, appuyez sur 4, Pour revenir en arrière, appuyez sur l'astérisque." --lang fr --output audio/fr/subcategory_fonio.wav;
gtts-cli "Quel type de Gombo voulez-vous acheter ? Pour Keleya appuyez sur 1, Pour Sabalibougou appuyez sur 2, Pour Gansourouni pressez 3, Pour tout autre type, appuyez sur 4, Pour revenir en arrière, appuyez sur l'astérisque." --lang fr --output audio/fr/subcategory_gombo.wav;
gtts-cli "Quel type de Mais voulez-vous acheter ? Pour Sotubaka appuyez sur 1, Pour Nieleni appuyez sur 2, Pour Dembaniouma pressez 3, Pour tout autre type, appuyez sur 4, Pour revenir en arrière, appuyez sur l'astérisque." --lang fr --output audio/fr/subcategory_mais.wav;
gtts-cli "Quel type de Sorgho voulez-vous acheter ? Pour Toroba appuyez sur 1, Pour Bobodje appuyez sur 2, Pour Tieblen pressez 3, Pour tout autre type, appuyez sur 4, Pour revenir en arrière, appuyez sur l'astérisque." --lang fr --output audio/fr/subcategory_sorgho.wav;
gtts-cli "Combien de kilos voulez-vous acheter? Veuillez indiquer le montant minimum, puis appuyez sur le HashTag." --lang fr --output audio/fr/quantity_min.wav;
gtts-cli "Combien de kilos voulez-vous acheter? Veuillez indiquer le montant maximum, puis appuyez sur le HashTag." --lang fr --output audio/fr/quantity_max.wav;
gtts-cli "Vous avez effectué la recherche suivante. Catégorie:" --lang fr --output audio/fr/results_category.wav;
gtts-cli "Sous-Catégorie:" --lang fr --output audio/fr/results_subcategory.wav;
gtts-cli "Quantité minimum:" --lang fr --output audio/fr/results_quantity_min.wav;
gtts-cli "Quantité maximum:" --lang fr --output audio/fr/results_quantity_max.wav;
gtts-cli "Pour écouter les résultats de votre recherche, appuyez sur 1. Pour effectuer une nouvelle recherche, appuyez sur l'astérisque" --output audio/fr/review_instructions.wav;
# - misc
gtts-cli "kilos" --lang fr --output audio/fr/kilos.wav;
gtts-cli "Quelque chose s'est mal passé, réessayez plus tard." --lang fr --output audio/fr/error.wav;
# - mock data
gtts-cli "Il existe une offre active correspondant à vos critères de recherche." --lang fr --output audio/fr/mock_result_1.wav;
gtts-cli "kilos de" --lang fr --output audio/fr/mock_result_2.wav;
gtts-cli "pour le prix de 500 francs." --lang fr --output audio/fr/mock_result_3.wav;
echo OK