package Backend

class EstimHousedata {

    /*fun aleaval():Int{
        return (50000..500000).random()
    }*/

    // Retourne L'estimation en Fonction des information données par l'utilisateur
    //et les coefficients du modèle d'apprenstissage
    fun estimation(surfacereelle : Double , type : Double, surfaceterrain: Double , nmdepiece : Double):Double{
        return 1310.48657149 * surfacereelle - 62415.26158975 * type + 71.08137866 * surfaceterrain - 10006.73241973 * nmdepiece  + 128303.21
        //surface reelle et surface terrain sont inversees
       // return surfacereelle + 2*  type +  3* surfaceterrain + 4*  nmdepiece
    }

}