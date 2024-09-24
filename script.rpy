# Definición de personajes
define p = Character("Protagonista")
define l = Character("Líder", color="#FF0000")
define d = Character("Doctor", color="#00FF00")
define r = Character("Rico", color="#FFD700")
define a = Character("Aliado", color="#6495ED")

# El juego comienza aquí.
label start:

    # Introducción del mundo en 2125
    scene bg city_dark with fade
    play music "cyberpunk_theme.mp3" fadein 2.0
    
    p "El año es 2125. La Tierra, devastada por una plaga alienígena, es ahora un lugar hostil."
    p "El 90 de la humanidad aún vive aquí, sobreviviendo como puede en un mundo donde la vegetación escasea."
    p "La gente rica, los afortunados, huyeron del planeta, viviendo en estaciones espaciales."
    p "Nosotros... los que quedamos, seguimos luchando."

    # Escena de la escuela
    scene bg cyberpunk with wipeleft
    
    p "Las escuelas nos enseñan solo lo necesario: no pensar, no cuestionar, solo obedecer y trabajar."
    p "La vida es un ciclo sin fin de supervivencia en este sistema roto."

    # Introducción del conflicto
    scene bg laboratory with dissolve
    show doctor at left
    
    d "La enfermedad alienígena sigue cobrando vidas."
    d "Pero creemos que la cura está en las pocas plantas que quedan."
    
    p "¿Las plantas? ¿Cómo es eso posible?"

    d "La naturaleza es lo único que puede detener el avance del virus. Dentro de estas cápsulas, llevamos semillas que pueden durar más de 100 años."
    
    p "¿Qué podemos hacer?"

    # Presentar el dilema del protagonista
    menu:
        "Ayudar a encontrar más semillas":
            jump ayudar_escena
        "Resignarse a sobrevivir":
            jump sobrevivir_escena

label ayudar_escena:
    scene bg wasteland with dissolve
    show aliado at right
    
    p "Salí a las tierras devastadas, buscando las últimas semillas de esperanza junto a un pequeño grupo de resistencia."
    a "Debemos movernos rápido, las tormentas radiactivas no tardarán en llegar."
    
    p "La radiación nos está matando lentamente, pero si encontramos esas semillas, tal vez podamos restaurar algo de lo que una vez fue la Tierra."
    
    # Encuentran un obstáculo en su misión
    scene bg wasteland_ruins with fade
    show ricos at left
    
    r "¿Crees que puedes simplemente tomar lo que queda de la Tierra y reclamarlo?"
    
    p "¿Quién eres tú?"

    r "Somos los guardianes del último vestigio de vida... los pocos ricos que no abandonamos el planeta. No permitiremos que los débiles destruyan lo que queda."

    p "No tenemos otra opción. Si no tomamos estas semillas, todos moriremos."

    # Opción de enfrentarse o huir
    menu:
        "Luchar por las semillas":
            jump luchar_semillas
        "Intentar negociar":
            jump negociar_semillas

label luchar_semillas:
    scene bg battle with fade
    p "Decidí que no hay tiempo para palabras. El conflicto se desató."
    p "Conseguimos las semillas, pero a un costo alto. Muchos no sobrevivieron."

    # Consecuencias de la decisión
    scene bg wasteland with dissolve
    show aliado at right
    
    a "Hemos pagado un alto precio. Tal vez las semillas nos den una oportunidad, pero ¿a qué costo?"
    
    p "La culpa me consume. Quizás haya tomado la decisión equivocada."

    # Reflexión sobre el futuro
    scene bg city_dark with fade
    p "Regresé a la ciudad con las semillas. Aunque hemos ganado, la victoria sabe a cenizas."
    p "¿Qué haremos ahora con las semillas? ¿Seremos capaces de restaurar la Tierra o es demasiado tarde?"

    return

label negociar_semillas:
    scene bg wasteland with dissolve
    p "Intenté razonar con ellos."
    
    r "Aceptamos ayudarte, pero habrá un precio. El futuro de la humanidad dependerá de lo que hagas con estas semillas."
    
    p "Sabía que no podíamos confiar en ellos, pero no había otra opción."

    # Consecuencias de la negociación
    scene bg laboratory with dissolve
    show doctor at left
    
    d "Las semillas están bajo el control de los ricos ahora. Trabajamos para ellos."
    
    p "¿Esto es lo que queríamos? Salvamos las semillas, pero ¿a qué costo?"

    p "Nos hemos convertido en sus peones, y ahora nuestro destino está en sus manos."

    return

label sobrevivir_escena:
    scene bg city_dark with dissolve
    p "Decidí seguir el ciclo, vivir un día más, pero algo dentro de mí se había roto."
    p "¿Cómo podría seguir adelante sabiendo que la última esperanza se desvanecía?"

    # Reflexión sobre la resignación
    scene bg wasteland with fade
    p "Vi cómo el mundo seguía muriendo lentamente. Quizás había una oportunidad de cambiar las cosas, pero la dejé pasar."

    p "Me convertí en una sombra de lo que una vez fui, un engranaje más en la máquina. ¿Hice lo correcto?"

    return
