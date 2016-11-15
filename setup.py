import cx_Freeze

executables = [cx_Freeze.Executable("Cars_Attack Project.py")]

cx_Freeze.setup(
    name="Cars Attack",
    options={"build_exe": {"packages":["pygame"],
                            "include_files":["sound_car_crash.ogg",
                                              "song_game.ogg", "veneno.png",
                                              "pista.jpg", "inimigo1.png",
                                              "inimigo2.png", "inimigo3.png",
                                              "inimigo4.png", "inimigo5.png",
                                              "inimigo6.png", "inimigo7.png",
                                              "inimigo8.png", "inimigo9.png",
                                              "inimigo10.png", "Lamborghini Veneno.jpg",
                                              "rank.jpg", "veneno_icon.png", "Record.txt",
                                              "High_Score.txt",]}},
    executables = executables

    )
