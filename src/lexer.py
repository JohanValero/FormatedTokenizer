import json
import re

# Carga el archivo de configuración JSON en formato UTF-8.
def loadJsonConfiguration():
    vData = None
    with open("./resources/configuration.json", encoding = "utf-8") as vFile:
        vData = json.load(vFile)
    return vData
gJsonConfiguration = loadJsonConfiguration()

# Se procesa una dirección en los diferentes Tokens de la dirección.
def pre_process_text(iAddress):
    # Se procesa toda la dirección en mayusculas, y se remueven
    # los espacios en blanco al inicio, al final y repetidos.
    vOutAddress = " ".join(iAddress.upper().strip().split())

    # Se remueven las vocales con acentos.
    vOutAddress = re.sub(r"[ÀÁÂÃÄÅ]", "A", vOutAddress)
    vOutAddress = re.sub(r"[ÈÉÊË]"  , "E", vOutAddress)
    vOutAddress = re.sub(r"[ÌÍÎÏ]"  , "I", vOutAddress)
    vOutAddress = re.sub(r"[ÒÓÔÕÖ]" , "O", vOutAddress)
    vOutAddress = re.sub(r"[ÙÚÛÜ]"  , "U", vOutAddress)

    # Se remueven los caracteres no deseados.
    vWordsToDelete = gJsonConfiguration["remove_chars"]
    for vKey in vWordsToDelete:
        vOutAddress = vOutAddress.replace(vKey, " ")
    
    # Separa una cadena de texto en subcadenas de texto y numericas.
    # Ejemplo: CALLE29I2#30-31, es separado en CALLE, 29, I, 2, #, 30, -, 31
    # Para que cada componente resultante se procesado como un Token diferente.
    vTokens = vOutAddress.split()
    vOutAddress = []
    for vToken in vTokens:
        if re.match(r"([A-Z]+[0-9]+|[0-9]+[A-Z]+)", vToken):
            vTokensResult = (segment for segment in re.split(r'([0-9]+\.?[0-9]*)', vToken) if segment)
            for vTemp in vTokensResult:
                vOutAddress.append(vTemp)
        else:
            vOutAddress.append(vToken)
    
    # Se reemplazan todas las variaciones conocidas de
    # los diferentes variaciones de un mismo token.
    # Ejemplo: CALLE, CALE, CL, CALLLE
    vVariations = gJsonConfiguration["clear_words"]
    vLexerTokens = []
    vLexerChar = "?"
    for i, vToken in enumerate(vOutAddress):
        for vCharVariation in vVariations:
            for vVariation in vCharVariation["words_variants"]:
                if vToken == vVariation:
                    vOutAddress[i] = vCharVariation["word_target"]
                    break
            if vOutAddress[i] == vCharVariation["word_target"]:
                vLexerChar = vCharVariation["word_lexer"]
        if vLexerChar == "?" and re.match("[0-9]+", vToken):
            vLexerChar = "#"
        
        vLexerTokens.append(vLexerChar)
        vLexerChar = "?"

    #print(">", " ".join(vOutAddress), "||", "".join(vLexerTokens))
    return (vOutAddress, vLexerTokens)