from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles



def reconnaissance_chiffre(self , liste_modeles , S):
    im_bin = self.binarisation(S)
    im_local = im_bin.localisation()
    sim = 0
    res=0
    for i in range(len(liste_modeles)):
        modele = liste_modeles[i]
        im_resized = im_local.resize(modele.H , modele.W)
        sim_i = im_resized.similitude(modele)
        if sim_i > sim:
            sim = sim_i
            res = i
    return res

