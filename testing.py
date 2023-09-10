home = {
    "Abraham": 1,
    "Godswill": 2,
    "Joel": 3,
    "Evan": 4,
    "Nehe": 5,
}

for p in home:
    print(p)
    print(home[p])


the_boys ={
    "Abraham":["Software Programming","Male","Tennis","24"],
    "Godswill":["Graphic Designing", "Male","Football","22"],
    "Joel":["Footballer","Male","Football","19"],
    "Evan":["Game Development","Male","Football","16"],
    "Nehemiah":["Primary School", "Male","Football",9],

}    

for d in the_boys:
    print(f"~{d}")
    for f in the_boys[d]:
        print(f"{f}")