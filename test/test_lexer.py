import sys

try:
    sys.path.insert(1, './src/')
    from lexer import pre_process_text
except (ModuleNotFoundError, ImportError) as e:
    print("{} failed".format(type(e)))
    exit(-1)

assert " ".join(pre_process_text("CÄrrera 18#12-56A   ")[0]) == "KR 18 12 56 A", "No estandarizó correctamente."
assert " ".join(pre_process_text("  calle18 n° 12  N - 56A")[0]) == "CL 18 12 N 56 A", "No estandarizó correctamente."
assert " ".join(pre_process_text("Transversal 88A con 70 Barrio 3 de octubre")[0]) == "TR 88 A 70 BR 3 DE OCTUBRE", "No estandarizó correctamente."
assert " ".join(pre_process_text("Carrera15#3B7A")[0]) == "KR 15 3 B 7 A", "No estandarizó correctamente."
assert " ".join(pre_process_text("calle29I2#30-31 Barrio Santa ana")[0]) == "CL 29 I 2 30 31 BR SANTA ANA", "No estandarizó correctamente."
assert " ".join(pre_process_text("Debajo de la alcaldía")[0]) == "DEBAJO DE LA ALCALDIA", "No estandarizó correctamente."

#assert " ".join(pre_process_text("CÄrrera 18#12-56A   ")[1]) == "K###?", "No tokenizó correctamente."
assert "".join(pre_process_text("  calle18 n° 12  N - 56A")[1]) == "Z##?#?", "No tokenizó correctamente."
assert "".join(pre_process_text("Transversal 88A con 70 Barrio 3 de octubre")[1]) == "A#?#B#??", "No tokenizó correctamente."
assert "".join(pre_process_text("Carrera15#3B7A")[1]) == "K##?#?", "No tokenizó correctamente."
assert "".join(pre_process_text("calle29I2#30-31 Barrio Santa ana")[1]) == "Z#?###B??", "No tokenizó correctamente."
assert "".join(pre_process_text("Debajo de la alcaldía")[1]) == "????", "No tokenizó correctamente."

print("Todos los test son OK")