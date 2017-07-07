exp_author = '((([A-Z][.][ ]+)+[a-zA-Z]+)(, ))*(and )?([A-Z][.][ ]+)+[a-zA-Z]+'
exp_coma = '[(,)[ ]+]?'
exp_title = '(((")[a-zA-Z ]+(,")( in )([a-zA-Z ]+))?|([a-zA-Z ]+)|((")[a-zA-Z]+(")))'
noPublicado = exp_author+exp_coma+exp_title+'( unpublished.)?'
#noPublicado = '([A-Z][.][ ]+[a-zA-Z]+)[(,)[ ]+]?(((")[a-zA-Z ]+(,")( in )([a-zA-Z ]+))?|([a-zA-Z ]+)|((")[a-zA-Z]+(")))( unpublished.)?'
#Ejemplo noPublicado
#B. Smith, "An approach to graphs of linear forms," unpublished.