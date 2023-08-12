meme_dict = {
             "CRINGE": "garip ya da utandırıcı bir davranış",
             "LOL" : "komik bir duruma verilen tepki (açılımı: Lots Of Laugh)",
             "IDK" : "bilmiyorum kelimesinin ingilizce karşılığı (I don't know)",
             "BRUH" : "rezil, utanç verici bir durum anında kullanılır",
             "DM" : "sosyal medya uygulamalarında mesaj anlamındadır"
}
for i in range(5):
    word = input ("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("lütfen kurallara uygun bir kelime yazdığınızdan emin olun")
