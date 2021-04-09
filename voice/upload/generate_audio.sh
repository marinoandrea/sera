#!/bin/sh

# english
gtts-cli 'Welcome to Sera! For English audio press 1, for French audio press 2.' --output audio/en/welcome.wav
gtts-cli "What type of Fonio do you want to sell? For Pon de Bore press 1, For Niatia press 2, For Banco Konkountre press 3, For any Other type press 4, To go back, press the asterisk." --output audio/en/subcategory_fonio.wav;
gtts-cli "What type of Gombo do you want to sell? For Keleya press 1, For Sabalibougou press 2, For Gansourouni press 3, For any Other type press 4, To go back, press the asterisk." --output audio/en/subcategory_gombo.wav;
gtts-cli "What type of Mais do you want to sell? For Sotubaka press 1, For Nieleni press 2, For Dembaniouma press 3, For any Other type press 4, To go back, press the asterisk." --output audio/en/subcategory_mais.wav;
gtts-cli "What type of Sorgho do you want to sell? For Toroba press 1, For Bobodje press 2, For Tieblen press 3, For any Other type press 4, To go back, press the asterisk." --output audio/en/subcategory_sorgho.wav;
gtts-cli "How many kilos do you want to sell? Insert the amount and then press the HashTag." --output audio/en/quantity.wav;
gtts-cli "At what price do you want to sell? Insert the price and then press the HashTag." --output audio/en/price.wav;
gtts-cli "You have selected the category:" --output audio/en/review_category.wav;
gtts-cli "You have selected the subcategory:" --output audio/en/review_subcategory.wav;
gtts-cli "You have selected the quantity:" --output audio/en/review_quantity.wav;
gtts-cli "You have selected the price:" --output audio/en/review_price.wav;
gtts-cli "Something went wrong, try again later." --output audio/en/error.wav;
gtts-cli "To confirm press 1, To listen again press the Hashtag, To go back press the Asterisk." --output audio/en/review_instructions.wav;
gtts-cli "Your announcement has been uploaded! Thank your for using Sera!" --output audio/en/review_sent.wav;

# french
gtts-cli "Bienvenue à Sera! Pour l'audio anglais, appuyez sur 1, pour l'audio français appuyez sur 2." --lang fr --output audio/fr/welcome.wav
gtts-cli "Quel type de Fonio voulez-vous vendre ? Pour Pon de Bore appuyez sur 1, Pour Niatia appuyez sur 2, Pour Banco Konkountre pressez 3, Pour tout autre type, appuyez sur 4, Pour revenir en arrière, appuyez sur l'astérisque." --lang fr --output audio/fr/subcategory_fonio.wav;
gtts-cli "Quel type de Gombo voulez-vous vendre ? Pour Keleya appuyez sur 1, Pour Sabalibougou appuyez sur 2, Pour Gansourouni pressez 3, Pour tout autre type, appuyez sur 4, Pour revenir en arrière, appuyez sur l'astérisque." --lang fr --output audio/fr/subcategory_gombo.wav;
gtts-cli "Quel type de Mais voulez-vous vendre ? Pour Sotubaka appuyez sur 1, Pour Nieleni appuyez sur 2, Pour Dembaniouma pressez 3, Pour tout autre type, appuyez sur 4, Pour revenir en arrière, appuyez sur l'astérisque." --lang fr --output audio/fr/subcategory_mais.wav;
gtts-cli "Quel type de Sorgho voulez-vous vendre ? Pour Toroba appuyez sur 1, Pour Bobodje appuyez sur 2, Pour Tieblen pressez 3, Pour tout autre type, appuyez sur 4, Pour revenir en arrière, appuyez sur l'astérisque." --lang fr --output audio/fr/subcategory_sorgho.wav;
gtts-cli "Combien de kilos voulez-vous vendre? Insérez le montant, puis appuyez sur le HashTag.." --lang fr --output audio/fr/quantity.wav;
gtts-cli "À quel prix voulez-vous vendre ? Insérez le prix, puis appuyez sur le HashTag." --lang fr --output audio/fr/price.wav;
gtts-cli "Vous avez sélectionné la catégorie:" --lang fr --output audio/fr/review_category.wav;
gtts-cli "Vous avez sélectionné type:" --lang fr --output audio/fr/review_subcategory.wav;
gtts-cli "Vous avez sélectionné la quantité:" --lang fr --output audio/fr/review_quantity.wav;
gtts-cli "Vous avez sélectionné le prix:" --lang fr --output audio/fr/review_price.wav;
gtts-cli "Quelque chose s'est mal passé, réessayez plus tard." --lang fr --output audio/fr/error.wav;
gtts-cli "Pour confirmer, appuyez sur 1, Pour réécouter, appuyez sur le Hashtag, Pour revenir en arrière, appuyez sur l'astérisque." --lang fr --output audio/fr/review_instructions.wav;
gtts-cli "Votre annonce a été téléchargée! Merci d'avoir utilisé Sera!" --lang fr --output audio/fr/review_sent.wav;
