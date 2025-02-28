kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

#invert the dictionnary

kata_r = {v: k for k, v in kata.items()}

print(f"{kata_r.get("Guido van Rossum")} was created by {kata["Python"]}"\
	  , f"{kata_r.get("Yukihiro Matsumoto")} was created by {kata["Ruby"]}"\
		, f"{kata_r.get("Rasmus Lerdorf")} was created by {kata["PHP"]}", sep="\n")