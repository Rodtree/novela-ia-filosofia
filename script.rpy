
# Definición de personajes# Definición de personajes
define k = Character("K")
define n = Character("Narrador")
define p = Character("Protagonista")
define l = Character("Líder", color="#FF0000")
define d = Character("Doctor", color="#00FF00")
define r = Character("Rico", color="#FFD700")
define a = Character("Aliado", color="#6495ED")



# El juego comienza aquí.
label start:

    # Introducción del mundo en 2157
    scene bg_city_devastated with fade
    play music "dystopia_theme.mp3" fadein 2.0
    
    n "El año es 2157. La Tierra está devastada."
    n "No quedan plantas. Los océanos son masas grises y tóxicas, y la atmósfera apenas sostiene la vida humana."
    n "La humanidad está dividida entre los millonarios que viven en estaciones espaciales autosuficientes y los pobres que se arrastran en un planeta moribundo."
    n "En este mundo, el recurso más preciado es la vegetación. Las plantas, la clave para transformar el aire contaminado y curar el virus alienígena que asola a la humanidad."

    # Cambio de escena - Introducción de Lara y Kai
    scene bg_shelter_underground with dissolve
    show p at left
    show k at right

    p "¿Has escuchado los rumores, Kai?"
    k "¿Sobre la cápsula del tiempo? Claro que sí. Todos hablan de ella últimamente."
    
    p "Dicen que contiene las últimas semillas del planeta... Si es cierto, esas semillas podrían salvarnos a todos."
    k "O podrían condenarnos. Sabes que si las estaciones espaciales se enteran, enviarán a sus mercenarios tras ellas."
    
    # Presentar el dilema del protagonista
    menu:
        "Decidir buscar la cápsula":
            jump buscar_capsula
        "Resignarse a la desesperanza":
            jump resignacion

label buscar_capsula:
    p "No podemos quedarnos aquí esperando morir. Tenemos que intentarlo. Debemos encontrar esa cápsula."
    k "Estoy contigo. Pero debemos ser cautelosos. No somos los únicos que la buscan."
    
    # Cambio de escena - La búsqueda comienza
    scene bg_wasteland_ruins with fade
    n "Lara y Kai partieron hacia las tierras devastadas, guiados por un rumor que podría ser su última esperanza."

    # Fin del capítulo
    n "Fin del Capítulo 1"
    return

label resignacion:
    p "Tal vez sea solo una leyenda... No podemos arriesgarnos, Kai. No ahora."
    k "Entiendo... Pero, ¿y si fuera verdad? Podríamos cambiarlo todo."
    
    p "No lo sé... No creo que tengamos otra opción que sobrevivir como podamos."

    # Fin del capítulo
    n "Fin del Capítulo 1"
    return

    # Continuación del guion de Lara y Kai

label capitulo_2:

    # Introducción del Capítulo 2
    scene bg_wasteland_ruins with fade
    play music "suspense_theme.mp3" fadein 2.0
    
    n "Capítulo 2: Un hallazgo peligroso"
    n "Después de semanas de búsqueda en las tierras devastadas, Lara y Kai descubren algo inesperado."

    # Encuentro de la cápsula del tiempo
    scene bg_ruined_city_cave with dissolve
    show p at left
    show k at right
    
    p "Mira, Kai... parece una cueva olvidada."
    k "No está en ningún mapa. Debe ser lo que estamos buscando."
    
    p "¡Aquí está! La cápsula del tiempo. No puedo creerlo..."
    
    # Descubrimiento de las semillas
    show p at left with dissolve
    show k at right with dissolve
    n "Lara y Kai abren la cápsula con cautela. Dentro encuentran una pequeña colección de semillas, envueltas en un papel antiguo que dice: 'La última esperanza de la Tierra'."

    p "Estas son... las últimas semillas del planeta."
    k "Tenemos que plantarlas cuanto antes, pero... debemos tener cuidado. Si las estaciones espaciales descubren esto, estaremos en peligro."
    
    # Presentar una decisión importante
    menu:
        "Decidir plantar las semillas en secreto":
            jump plantar_secreto
        "Esperar y planificar cuidadosamente":
            jump esperar_planificar

label plantar_secreto:
    scene bg_wasteland_secret_spot with fade
    n "Lara y Kai encuentran un lugar secreto para plantar las semillas, esperando poder mantenerlas ocultas de los mercenarios de las estaciones espaciales."
    
    p "Si estas semillas brotan, podríamos tener una oportunidad real de cambiar el destino de la Tierra."
    k "Es un riesgo... pero no tenemos otra opción."

    # Descubrimiento de los mercenarios
    scene bg_wasteland with dissolve
    show m at right
    
    m "¿Pensaban que podrían ocultar algo tan importante de nosotros?"
    
    p "¡Nos han seguido!"
    
    n "Los mercenarios han estado observando a Lara y Kai, y ahora planean apoderarse de las semillas."

    # Escena de acción
    scene bg_battle with fade
    p "No podemos dejar que se lleven las semillas. ¡Debemos luchar!"
    
    # Fin del Capítulo 2
    n "Fin del Capítulo 2: Perseguidos desde las estrellas."
    return

label esperar_planificar:
    scene bg_ruined_city_cave with fade
    p "No podemos apresurarnos. Debemos pensar bien en nuestro próximo movimiento."
    k "De acuerdo. Si nos movemos ahora, los mercenarios podrían encontrarnos fácilmente."

    n "Deciden esperar y planificar cuidadosamente sus próximos pasos, conscientes del peligro que acecha."

    # Fin del Capítulo 2
    n "Fin del Capítulo 2: Perseguidos desde las estrellas."
    return
# Continuación del guion de Lara y Kai

label capitulo_3:

    # Introducción del Capítulo 3
    scene bg_wasteland_desert with fade
    play music "action_theme.mp3" fadein 2.0
    
    n "Capítulo 3: Perseguidos desde las estrellas"
    n "Esa misma noche, la estación espacial Elysium lanza un operativo en la Tierra, enviando mercenarios para capturar las semillas."

    # Cambio de escena: Los mercenarios aparecen
    scene bg_wasteland_ruins with dissolve
    show p at left
    show k at right
    show m at right with fade
    
    m "Ríndanse. No hay dónde esconderse. Las semillas pertenecen a quienes saben cómo usarlas."
    
    p "¡No puedes arrebatarnos esto! Estas semillas son la última esperanza para todos."
    m "No se trata de esperanza, niña. Se trata de poder."

    # Opción para huir o enfrentarse
    menu:
        "Huir hacia el desierto":
            jump huir_desierto
        "Enfrentarse a los mercenarios":
            jump enfrentarse_mercenarios

label huir_desierto:
    scene bg_desert_night with dissolve
    n "Lara y Kai escapan hacia el desierto que antes fue un bosque frondoso, perseguidos por drones de vigilancia y mercenarios despiadados."

    p "Tenemos que alejarnos lo más rápido posible. El desierto no es seguro, pero es nuestra única opción."
    k "No podemos dejarlos seguirnos hasta nuestro escondite. ¡Debemos despistarlos!"

    # Cambio de escena - Carrera por el desierto
    scene bg_desert_dunes with fade
    play sound "drone_sound.mp3"
    
    n "Drones sobrevolaban el cielo, buscando a Lara y su equipo."
    
    p "¡Allí! Un cañón. Si llegamos, podremos ocultarnos."

    # Escena de tensión: logran escapar por poco
    scene bg_desert_canyon with dissolve
    stop sound fadeout 1.0
    
    k "Lo logramos... por ahora."
    p "Debemos mantenernos ocultos y planificar el próximo movimiento."

    # Fin del Capítulo 3: Escaparon, pero siguen en peligro
    n "Fin del Capítulo 3: El desierto no ofrece refugio."
    return

label enfrentarse_mercenarios:
    scene bg_battle with fade
    n "Decidieron no huir. La confrontación con los mercenarios era inevitable."
    
    p "¡No nos rendiremos sin pelear!"
    
    show m at right with dissolve
    m "Ustedes son una molestia. Nos desharemos de ustedes."

    # Escena de batalla
    p "Luchamos con todo lo que teníamos, pero su tecnología y armamento eran superiores."

    scene bg_after_battle with dissolve
    show p at left
    show k at right

    k "Hemos perdido a varios de los nuestros..."
    p "Pero tenemos las semillas. Eso es lo más importante."

    n "A un gran costo, Lara y Kai lograron derrotar a los mercenarios. Sabían que la guerra no había terminado, pero habían ganado una pequeña victoria."

    # Fin del Capítulo 3: Ganaron, pero a un gran costo
    n "Fin del Capítulo 3: Una victoria amarga."
    return
# Continuación de la historia en Ren'Py

label capitulo_4:

    # Introducción del Capítulo 4
    scene bg_desert with fade
    play music "ambient_mystery.mp3" fadein 2.0
    
    n "Capítulo 4: La primera planta"
    n "Después de huir de los mercenarios, Lara y Kai encuentran un pequeño oasis en el desierto. Un lugar con una fuente subterránea, ideal para plantar la primera semilla."

    # Escena en el oasis
    scene bg_oasis with dissolve
    show p at left
    show k at right
    
    p "Este parece el lugar adecuado. Si la semilla puede sobrevivir aquí, tal vez tengamos una oportunidad."
    
    k "Lo sé... pero me preocupa lo que pueda suceder si plantamos esta semilla. No sabemos los efectos secundarios."

    # Momento de plantar la semilla
    show p at center
    p "No tenemos otra opción. Debemos arriesgarnos."

    # Escena de la semilla siendo plantada
    scene bg_oasis with fade
    play sound "plant_seed.mp3"
    
    n "Lentamente, Lara planta la primera semilla en la tierra húmeda. Minutos después, algo extraordinario sucede: un pequeño brote verde emerge del suelo."

    p "¡Está creciendo! No puedo creerlo..."
    k "Es increíble. Nunca pensé que vería algo así en mi vida."

    # La planta empieza a tener efectos
    scene bg_oasis with dissolve
    show p at left
    show k at right
    show plant_small at center
    
    p "Mira... la planta está absorbiendo el aire envenenado a su alrededor."
    k "Es verdad. Se siente más limpio... pero, espera..."
    
    # Momento de tensión: El efecto secundario del CO2
    p "Algo no está bien. La planta está expulsando dióxido de carbono... en grandes cantidades."
    k "Esto podría ser un problema. Si plantamos más de estas semillas, podríamos empeorar la atmósfera en lugar de mejorarla."

    # Reflexión sobre los riesgos
    p "¿Qué hacemos ahora? Necesitamos más de estas plantas para curar a los infectados, pero si seguimos así, podríamos destruir lo poco que queda de la atmósfera."
    
    k "No tenemos otra opción por ahora. Debemos proteger esta planta, pero ser conscientes de los riesgos."

    # Decisión: Proteger la planta o destruirla
    menu:
        "Proteger la planta a toda costa":
            jump proteger_planta
        "Destruir la planta antes de que sea demasiado tarde":
            jump destruir_planta

label proteger_planta:
    scene bg_oasis_night with fade
    n "Lara y Kai deciden proteger la planta. Saben que es su única esperanza de curar a los infectados, a pesar del peligro."

    p "No podemos darnos el lujo de destruir la planta. Necesitamos tiempo para encontrar una solución."
    k "De acuerdo. Pero debemos estar listos para cualquier cosa. Si la atmósfera empeora, no tendremos oportunidad."

    # Fin del Capítulo 4: Protegiendo la planta
    n "Lara y Kai montan guardia alrededor de la planta. Saben que los mercenarios aún los buscan, pero por ahora, su prioridad es preservar lo único que podría salvarlos."
    
    return

label destruir_planta:
    scene bg_oasis_night with fade
    n "Lara, con el corazón pesado, decide destruir la planta. Sabe que podría salvar vidas, pero también destruir el poco aire respirable que queda en la Tierra."

    show p at center
    p "No puedo arriesgarme. Si seguimos plantando estas semillas, podríamos condenar a todos."
    k "Entiendo... es una decisión difícil, pero tal vez sea lo correcto."

    play sound "destroy_plant.mp3"

    # Fin del Capítulo 4: La planta destruida
    n "Con lágrimas en los ojos, Lara destruye la planta. Saben que ahora su única esperanza es encontrar una manera de curar el virus sin envenenar la atmósfera."
    
    return

# Continuación de la historia en Ren'Py

label capitulo_5:

    # Introducción del Capítulo 5
    scene bg_night_camp with fade
    play music "dark_suspense.mp3" fadein 2.0
    
    n "Capítulo 5: Traición en las sombras"
    n "Tras plantar la primera semilla, Lara y su equipo montan un campamento para descansar. La tensión es palpable, y el miedo a ser encontrados por los mercenarios los mantiene en alerta."

    # Conversación en el campamento
    show p at left
    show k at right
    show sarah at center
    
    p "No sé cuánto tiempo más podremos mantener esto en secreto. Si los mercenarios nos encuentran, no tendremos escapatoria."
    
    k "Lo sé... pero aún necesitamos tiempo para averiguar cómo lidiar con los efectos de la planta. No podemos simplemente rendirnos ahora."
    
    show sarah at center with dissolve
    sarah "Estamos demasiado cerca de lograr algo grande. Debemos mantenernos unidos."

    # Ataque repentino
    play sound "explosion.mp3"
    scene bg_camp_attack with flash
    show leon at right

    n "De repente, una explosión sacude el campamento. Los mercenarios de León Novak han encontrado a Lara y su equipo. Comienza un ataque brutal."
    
    p "¡Nos han encontrado! ¡A cubierto!"
    k "¡Maldición! Sabía que no estaríamos a salvo por mucho tiempo."
    
    # Traición de Sarah
    scene bg_camp_attack with dissolve
    show sarah at center
    show leon at right
    
    sarah "Lara... lo siento."
    p "¿Qué estás diciendo?"
    
    sarah "Nunca te dije toda la verdad. Desde el principio, estuve trabajando para Novak. Mi misión era asegurarme de que las semillas llegaran a manos de la élite."
    
    p "¡No puede ser! ¡Confiábamos en ti!"
    
    leon "Sarah ha hecho su trabajo a la perfección. Ahora, entreguen las semillas o no dejaré a nadie vivo."

    # Decisión del jugador: Confiar en Kai para desactivar los drones o enfrentarse a León
    menu:
        "Confiar en Kai para desactivar los drones":
            jump desactivar_drones
        "Enfrentarse a León directamente":
            jump enfrentarse_a_leon

label desactivar_drones:
    scene bg_camp_attack with dissolve
    show k at right
    show p at left
    show leon at center
    
    n "Kai, con rapidez, intenta hackear los drones de vigilancia para neutralizar la ventaja de los mercenarios."
    
    k "¡Estoy casi ahí! Necesito unos segundos más..."
    p "¡Rápido, Kai! ¡Nos están superando!"

    play sound "drone_shutdown.mp3"

    n "De repente, los drones caen del cielo, desactivados. Lara y su equipo aprovechan la confusión para escapar."
    
    scene bg_desert_night with fade
    show p at left
    show k at right
    
    p "Gracias a Kai, hemos logrado escapar. Pero Sarah se ha llevado una de las semillas... no puedo creer que haya traicionado a su propia gente."

    return

label enfrentarse_a_leon:
    scene bg_camp_attack with dissolve
    show leon at right
    show p at left
    show sarah at center
    
    p "¡No permitiré que te lleves las semillas, León!"
    
    leon "Te admiro, Lara. Pero no tienes ninguna oportunidad."
    
    # Lucha con los mercenarios
    scene bg_battle_night with fade
    play sound "gunfire.mp3"
    
    n "Lara decide enfrentarse directamente a León y sus mercenarios. Una feroz batalla comienza, pero son superados en número."

    show p at left
    show k at right
    
    p "¡No vamos a rendirnos sin pelear!"
    k "Es una locura, pero no hay otra opción."
    
    # Consecuencias de la batalla
    scene bg_camp_aftermath with fade
    show p at left
    show k at right
    
    n "La batalla termina en una derrota. Varios miembros del equipo caen, y en medio del caos, Sarah escapa con una de las semillas."
    
    p "Perdimos a muchos... y Sarah nos traicionó. Debimos haberlo visto venir."
    k "Aún podemos continuar, pero será más difícil de lo que pensábamos."

    return

# Continuación de la historia en Ren'Py

label capitulo_6:

    # Introducción del Capítulo 6
    scene bg_wasteland_morning with fade
    play music "tension_theme.mp3" fadein 2.0
    
    n "Capítulo 6: El costo de la vida"
    n "Después de plantar las primeras semillas y escapar de los mercenarios, Lara y su equipo se refugian en las tierras desérticas. La atmósfera se vuelve cada vez más tóxica, pero el virus alienígena parece retroceder lentamente."

    show p at left
    show k at right

    p "No puedo negar lo que hemos visto. Las plantas están curando a la gente del virus, pero el aire... cada vez es más difícil respirar."
    
    k "Sabíamos que habría consecuencias. El dióxido de carbono está aumentando peligrosamente. No sé cuánto tiempo podremos soportarlo."

    p "Estamos perdiendo el control de la situación. Si seguimos plantando, podríamos destruir la poca atmósfera que queda."

    # Encuentro con sobrevivientes curados
    scene bg_forest_dead with dissolve
    show survivors at center

    n "En su viaje, Lara y Kai se encuentran con un grupo de sobrevivientes. Algunos de ellos fueron infectados por el virus, pero gracias a las plantas, han comenzado a recuperarse."

    show survivor_1 at center
    
    survivor_1 "Nos han salvado... ya no sentimos los síntomas del virus. Estamos eternamente agradecidos."

    p "¿Cuántos más están curados?"
    
    survivor_1 "Decenas de nosotros... pero también hemos notado que el aire se está volviendo más pesado. Nos cuesta respirar."

    show k at right
    
    k "Lo sabíamos, pero escucharlo de ellos lo hace más real. Debemos tomar una decisión, Lara. ¿Seguimos plantando las semillas, o encontramos otra solución?"

    # Dilema sobre las plantas y el aire tóxico
    menu:
        "Seguir plantando las semillas para salvar más vidas":
            jump seguir_plantando
        "Detener el uso de las semillas para preservar el aire":
            jump detener_plantacion

label seguir_plantando:
    scene bg_forest_dead with fade
    show p at left
    show k at right
    
    p "No podemos detenernos ahora. Cada día que pasa, más personas se curan. Las plantas son nuestra única esperanza."
    
    k "Lo entiendo, pero el aire... si no hacemos algo pronto, la atmósfera será inhabitable."
    
    p "Si dejamos de plantar, todos morirán por el virus. No hay otra opción."

    # Consecuencias de seguir plantando
    scene bg_wasteland with fade
    show k at right
    show p at left
    
    n "Lara y Kai continúan plantando más semillas. A medida que más personas se curan, la atmósfera sigue deteriorándose. Las tormentas de polvo aumentan, y el cielo se oscurece."

    show survivor_2 at center
    
    survivor_2 "¡Gracias a las plantas, estoy curado! Pero... el aire... no puedo respirar."
    
    p "Hicimos lo que teníamos que hacer. Pero no sé cuánto más podremos sobrevivir en este mundo envenenado."

    return

label detener_plantacion:
    scene bg_wasteland with dissolve
    show p at left
    show k at right
    
    p "No podemos seguir plantando. El costo es demasiado alto. Si seguimos así, no quedará aire para respirar."
    
    k "Es la decisión correcta, pero significa que muchas personas seguirán sufriendo por el virus."

    p "Es un sacrificio que tendremos que hacer. Necesitamos encontrar otra solución, o tal vez dejar de luchar contra lo inevitable."

    # Consecuencias de detener la plantación
    scene bg_camp_night with fade
    show k at right
    show p at left
    
    n "Lara decide detener el uso de las semillas. Aunque logran preservar lo que queda de la atmósfera, el virus sigue avanzando, afectando a más personas. Los sobrevivientes miran a Lara en busca de esperanza."

    show survivor_1 at center
    
    survivor_1 "¿Por qué nos has abandonado? Las plantas eran nuestra única esperanza..."

    p "No fue una decisión fácil, pero el costo era demasiado alto. No quiero que todos muramos por falta de aire."

    show k at right
    
    k "Espero que hayas tomado la decisión correcta, Lara. Solo el tiempo lo dirá."

    return

# Continuación de la historia en Ren'Py

label capitulo_7:

    # Introducción del Capítulo 7
    scene bg_desert_storm with fade
    play music "desperation_theme.mp3" fadein 2.0
    
    n "Capítulo 7: Un último sacrificio"
    n "Las consecuencias del uso de las semillas se han desatado. El aire en la Tierra se vuelve cada vez más tóxico, las tormentas de polvo cubren el cielo y la vida se está desmoronando. Lara sabe que la última semilla podría ser la clave para el futuro, pero el costo es demasiado alto."

    show p at left
    show k at right
    
    p "El aire se está volviendo irrespirable. No queda mucho tiempo."
    
    k "La última semilla está en manos de Novak. Si logramos recuperarla, podríamos salvar lo que queda... pero si la plantamos, el aire será nuestra sentencia de muerte."

    p "No podemos dejar que ellos tengan la semilla. Los ricos la usarán para perpetuar su dominio desde el espacio. Pero ¿podemos sacrificar lo que queda de la Tierra?"

    # Plan para recuperar la semilla
    scene bg_camp_night with dissolve
    show survivors at center
    
    n "Lara y Kai reúnen a los pocos sobrevivientes que quedan. Deciden organizar un ataque final para recuperar la semilla de las manos de Novak y sus mercenarios."

    show p at left
    show a at right
    
    p "Esta es nuestra última oportunidad. Si fallamos, no habrá más esperanza."

    a "No hay vuelta atrás. Estamos contigo, Lara, hasta el final."

    # Asalto al campamento de Novak
    scene bg_military_base with fade
    play music "battle_theme.mp3" fadein 2.0
    
    n "El grupo de Lara se infiltra en el campamento de Novak bajo la cobertura de la noche. Los mercenarios están alerta, pero no esperan un ataque directo. Se desata una feroz batalla."

    show p at left
    show novak at right
    
    p "¡Novak! ¡Devuélvenos la semilla!"
    
    novak "¿De verdad crees que te la voy a entregar, niña? Esta semilla es poder, y no permitiré que tú ni nadie más decida su destino."

    # Confrontación final con Novak
    menu:
        "Luchar contra Novak por la semilla":
            jump luchar_novak
        "Intentar razonar con Novak":
            jump razonar_novak

label luchar_novak:
    scene bg_battle with fade
    show p at left
    show novak at right
    
    p "No hay más palabras. La batalla final ha comenzado."
    
    n "Lara lucha ferozmente contra Novak y sus mercenarios. La violencia se intensifica, y varios miembros del equipo caen. En el último momento, Lara logra derrotar a Novak y toma la semilla."

    show p at center
    
    p "Lo logramos... pero ¿a qué costo?"

    jump sacrificio_semilla

label razonar_novak:
    scene bg_military_base with dissolve
    show p at left
    show novak at right
    
    p "Esto tiene que terminar, Novak. Si seguimos así, nadie sobrevivirá. La semilla no puede ser utilizada para beneficio de unos pocos."
    
    novak "¿Y quién eres tú para decidir eso? Esta es la única esperanza que nos queda, y no permitiré que caiga en manos equivocadas."

    p "No es cuestión de poder o control. Es cuestión de supervivencia. Si plantamos la semilla, condenaremos a la Tierra, pero si la destruyes, también condenarás a todos."

    n "Por un momento, Novak duda. Las palabras de Lara resuenan en su mente, pero su ambición es más fuerte. Sin embargo, al final, Lara logra convencerlo de que le entregue la semilla, aunque con desconfianza."

    show novak at right
    novak "Toma la semilla. Pero recuerda mis palabras, niña. Al final, no importa lo que hagas... el poder siempre encuentra su camino."

    jump sacrificio_semilla

label sacrificio_semilla:
    # El sacrificio final de Lara
    scene bg_wasteland with fade
    show p at left
    show k at right
    
    p "Tenemos la última semilla... pero no podemos plantarla. Si lo hacemos, la Tierra será inhabitable."

    k "Entonces, ¿qué hacemos? ¿La destruimos?"

    p "Es nuestra única opción. Si permitimos que los ricos la usen, se aprovecharán de su poder, y si la plantamos, condenaremos lo que queda de la atmósfera."

    show p at center
    p "Lo siento... pero no hay otra manera."

    n "Con una mezcla de tristeza y determinación, Lara destruye la última semilla, sabiendo que este sacrificio es lo único que puede evitar una catástrofe mayor. El destino de la Tierra está sellado."

    scene bg_city_dark with fade
    show p at left
    show k at right
    
    p "No sé si tomé la decisión correcta, pero lo que hicimos fue necesario."

    k "Sobrevivimos, pero... ¿por cuánto tiempo más?"

    n "El cielo se oscurece aún más, el aire se vuelve cada vez más pesado, y la lucha por la supervivencia continúa. Aunque el virus ha sido contenido, la atmósfera está en un punto crítico."

    return

# Continuación de la historia en Ren'Py

label capitulo_8:

    # Introducción del Capítulo 8
    scene bg city_dark with fade
    play music "melancholy_theme.mp3" fadein 2.0
    
    n "Capítulo 8: El eco de la esperanza"
    n "Lara y su equipo observan cómo la Tierra se desmorona lentamente. La atmósfera sigue deteriorándose, pero el sacrificio de la última semilla les ha dado algo más que sólo sobrevivir: les ha dado tiempo."

    show p at left
    show k at right
    
    p "Destruir la semilla fue la decisión más difícil que he tenido que tomar. La lucha sigue, pero al menos no hemos entregado el poder a aquellos que solo buscan control."

    k "El costo fue alto, pero no estábamos listos para permitir que el poder cayera en manos equivocadas. Pero, ¿qué haremos ahora? La Tierra se está desvaneciendo."

    # Reflexiones sobre el futuro
    scene bg wasteland with dissolve
    n "La vida en la Tierra se reduce a una sombra de lo que una vez fue. Las tormentas son más frecuentes, el aire más denso, y la desesperación se siente en cada rincón."

    show p at left
    
    p "Hay un susurro en el viento... un eco de lo que fue la vida. A veces, me pregunto si alguna vez volveremos a vivir en armonía con la naturaleza."

    k "¿Crees que será posible? ¿Podremos algún día recuperar lo que perdimos?"

    p "No lo sé. Pero creo que hay esperanza. Tal vez, en algún momento, la humanidad aprenderá a coexistir con el planeta."

    # Encuentro con otros sobrevivientes
    scene bg ruins with fade
    show survivors at center
    
    n "A medida que Lara y Kai recorren las ruinas de su hogar, encuentran a otros sobrevivientes que han logrado resistir. Se organizan, compartiendo recursos y conocimiento, tratando de sobrevivir juntos."

    show a at left
    show d at right
    
    a "Podemos trabajar juntos. Cada pequeña acción puede marcar la diferencia. Tal vez un día, podamos replantar la vida en esta Tierra."

    d "La ciencia puede ayudarnos a entender cómo restaurar el equilibrio. No estamos solos en esto."

    # Un último mensaje de esperanza
    scene bg night_sky with dissolve
    show p at center
    
    p "Tal vez hemos perdido la batalla, pero no la guerra. Cada día es una nueva oportunidad para aprender de nuestros errores y construir un futuro mejor."

    n "La historia de la humanidad está llena de altibajos, pero el espíritu de lucha sigue vivo en aquellos que se niegan a rendirse."

    p "Y así, mientras el viento susurra entre las ruinas, la esperanza perdura. Un día, la Tierra volverá a ser verde, y tal vez, solo tal vez, encontraremos una manera de vivir en armonía con la naturaleza nuevamente."

    # Reflexión final
    scene bg city_dark with fade
    p "El susurro del viento es lo único que queda de la Tierra, pero el legado verde de las semillas perdurará en la memoria de quienes lucharon por un futuro mejor."

    n "Y aunque el futuro es incierto, la lucha por la vida, la esperanza y la conexión con la naturaleza sigue siendo el corazón de la humanidad."

    # Final del juego
    n "FIN"
    
    return

