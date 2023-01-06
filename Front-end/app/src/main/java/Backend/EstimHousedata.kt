package Backend

class EstimHousedata {

    /*fun aleaval():Int{
        return (50000..500000).random()
    }*/
    
    // Retourne L'estimation en Fonction des information données par l'utilisateur 
    //et les coefficients du modèle d'apprenstissage
    
    fun estimation(surfacereelle:Int , type : Int, surfaceterrain: Int , nmdepiece : Int):Int{
        return (1310 * surfacereelle - 62415 * type + 71 * surfaceterrain - 10006 * nmdepiece )
    }

}
