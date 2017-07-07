from control import paperDirector

paperApa = paperDirector.paperDirector(1,"mi titulo es este","Ecuador","Guayaquil")


texto = "@article{mi article,  author  = {Peter Adams},   title   = {The title of the work},  journal = {The name of the journal},  year    = 1993,  number  = 2,  pages   = {201-213},  month   = 7,  note    = {An optional note},   volume  = 4}"

texto2 = "@conference{mis conference,  author       = {Peter Draper},   title        = {The title of the work},  booktitle    = {The title of the book},  year         = 1993,  editor       = {The editor},  volume       = 4,  series       = 5,  pages        = 213,  address      = {The address of the publisher},  month        = 7,  organization = {The organization},  publisher    = {The publisher},  note         = {An optional note}  }"

texto3 = "@book{mi book,  author    = {Peter Babington},   title     = {The title of the work},  publisher = {The name of the publisher},  year      = 1993,  volume    = 4,  series    = 10,  address   = {The address},  edition   = 3,  month     = 7,  note      = {An optional note},  isbn      = {3257227892}}"

texto4 = "@manual{mi manual,  title        = {The title of the work},  author       = {Peter Gainsford},   organization = {The organization},  address      = {The address of the publisher},  edition      = 3,  month        = 7,  year         = 1993,  note         = {An optional note}}"

texto5 = "@unpublished{mi unpublished,  author       = {Peter Marcheford},   title        = {The title of the work},  note         = {An optional note},  month        = 7,  year         = 1993}"

paperApa.iniciarBibtex_compiler_add_referencias(5,texto5)
paperApa.iniciarBibtex_compiler_add_referencias(4,texto4)
paperApa.iniciarBibtex_compiler_add_referencias(3,texto2)
paperApa.iniciarBibtex_compiler_add_referencias(2,texto3)
paperApa.iniciarBibtex_compiler_add_referencias(1,texto)

paperApa.paper.addIntro("Actualmente estamos viviendo una gran revolución de la información sin darnos cuenta y sin conocer totalmente la tecnología que nos rodea. Nuevos cambios hacen que tengamos que actualizarnos constantemente en conocimientos relacionados con las nuevas tecnologías")
paperApa.paper.addPalabraClaves("tecnologia")
paperApa.paper.addPalabraClaves("sociedad")
paperApa.paper.addPalabraClaves("viviendo")

paperApa.paper.addAbstract("People, both those who are studying and those who have already completed their learning stage, have an obligation to know more and more about the operation of new technologies. Why, really, if we want to compete in the future in a labor market like the one we are in today, it is essential to be up to date.")
paperApa.paper.addKeyWorks("technology")
paperApa.paper.addKeyWorks("society")
paperApa.paper.addKeyWorks("living")

paperApa.paper.addAutor("Jonathan Quintana")
paperApa.paper.addAutorCorporativo("Tribuna Salamanca org")

paperApa.paper.addResumen("Las personas, tanto las que están estudiando como las que ya han finalizado su etapa de aprendizaje, tenemos la obligación de conocer cada vez más sobre el funcionamiento de las nuevas tecnologías. ¿Por qué?, realmente si queremos competir en un futuro en un mercado laboral como en el que nos encontramos hoy en día es fundamental estar actualizado.")

paperApa.paper.addCuerpo("Tenemos, es más, necesitamos, desarrollar nuevas capacidades para poder competir en el mercado laboral, ademas de aprender a manejar diferentes equipos tecnológicos ya que estos forman parte de nuestra vida cotidiana.")
paperApa.paper.addCuerpo("Las nuevas tecnologías, relacionadas con nuestro entorno, están agilizando, optimizando y perfeccionando algunas actividades que realizamos en nuestro día a día. La comunicación en la actualidad es algo que ha avanzado mucho, una comunicación que es mucho más rápida que antes, un ejemplo de comunicación actual, en concreto a través de Internet, en el caso de transmitir mensajes, imágenes, vídeos y todo tipo de documentos desde diferentes partes del mundo durante las 24 horas del día es algo que ha desplazado un poco el envío de documentos por medio del servicio postal convencional.")
paperApa.paper.addCuerpo("Los nuevos aparatos electrónicos, de los que estamos constantemente rodeados, nos permiten realizar tareas que se hacían de forma manual, eso sí, de una forma más ágil y eficaz.")
paperApa.paper.addCuerpo("La tecnología juega un papel muy importante en el mundo desde el momento en que se crea un algo innovador que todos queremos tener cuanto antes. Todos queremos estar a la moda y presumir de tener lo último del mercado.")

paperApa.paper.addSubtitulo("Mi sbtitulo")

paperApa.paper.addRecomendaciones("recomendacion 1")
paperApa.paper.addRecomendaciones("recomendacion 2")
paperApa.paper.addRecomendaciones("recomendacion 3")

paperApa.paper.addConclusiones("conclusion 1")
paperApa.paper.addConclusiones("conclusion 2")
paperApa.paper.addConclusiones("conclusion 3")

paperApa.paper.addMail("jiquinta@espol.edu.ec")


paperApa.paper.crearPdf("Paper_Apa","Este es el titulo de mi paper")








