# author @aesha98
# Day 3: Treasure Island


#display ascii art

print('''
                        /\
                        ||
                        ||
                        ||
                        ||                                               ~-----~
                        ||                                            /===--  ---~~~
                        ||                   ;'                 /==~- --   -    ---~~~
                        ||                (/ ('              /=----         ~~_  --(  '
                        ||             ' / ;'             /=----               \__~
     '                ~==_=~          '('             ~-~~      ~~~~        ~~~--\~'
     \\                (c_\_        .i.             /~--    ~~~--   -~     (     '
      `\               (}| /       / : \           / ~~------~     ~~\   (
      \ '               ||/ \      |===|          /~/             ~~~ \ \(
      ``~\              ~~\  )~.~_ >._.< _~-~     |`_          ~~-~     )\
       '-~                 {  /  ) \___/ (   \   |` ` _       ~~         '
       \ -~\                -<__/  -   -  L~ -;   \\    \ _ _/
       `` ~~=\                  {    :    }\ ,\    ||   _ :(
        \  ~~=\__                \ _/ \_ /  )  } _//   ( `|'
        ``    , ~\--~=\           \     /  / _/ / '    (   '
         \`    } ~ ~~ -~=\   _~_  / \ / \ )^ ( // :_  / '
         |    ,          _~-'   '~~__-_  / - |/     \ (
          \  ,_--_     _/              \_'---', -~ .   \
           )/      /\ / /\   ,~,         \__ _}     \_  "~_
           ,      { ( _ )'} ~ - \_    ~\  (-:-)       "\   ~ 
                  /'' ''  )~ \~_ ~\   )->  \ :|    _,       " 
                 (\  _/)''} | \~_ ~  /~(   | :)   /          }
                <``  >;,,/  )= \~__ {{{ '  \ =(  ,   ,       ;
               {o_o }_/     |v  '~__  _    )-v|  "  :       ,"
               {/"\_)       {_/'  \~__ ~\_ \\_} '  {        /~\
               ,/!          '_/    '~__ _-~ \_' :  '      ,"  ~ 
              (''`                  /,'~___~    | /     ,"  \ ~' 
             '/, )                 (-)  '~____~";     ,"     , }
           /,')                    / \         /  ,~-"       '~'
       (  ''/                     / ( '       /  /          '~'
    ~ ~  ,, /) ,                 (/( \)      ( -)          /~'
  (  ~~ )`  ~}                   '  \)'     _/ /           ~'
 { |) /`,--.(  }'                    '     (  /          /~'
(` ~ ( c|~~| `}   )                        '/:\         ,'
 ~ )/``) )) '|),                          (/ | \)                 The Threshing
  (` (-~(( `~`'  )                        ' (/ '
   `~'    )'`')                              '
     ` ``
''')


# display welcome message
welcome = 'Welcome To The Threshing\n\n'
game_info = 'A dragon without their rider is a tragedy, and a rider without their dragon is dead\nYour mission is to survive the threshing. Are you worthy enough? Choose wisely.\n'

print(welcome + game_info) 

#display first choice
first_choice = input('You are at a crossroads. Where do you want to go?\n Type "left" or "right"\n')

if (first_choice == "left"):
	  
    second_choice = input("You keep running and find yourself ashore, no boats available. The next boat is in 10 minutes. Do you swim or wait?\n")
	  
    if(second_choice == "wait"):
        
        final_choice = input("You decided to wait, and take the next boat.\n You finally reached an island. There, you saw three door. Red, Blue and Yellow. Which one do you open?\n")

        if (final_choice == "red"):
                print("You got yourself a mighty, fierce and brave dragon! Congrats, but you can do better")
        elif(final_choice == "yellow"):
                print("You are the chosen one! you got yourself a legend dragon, who is impressed by your courage throughout the trial.\nCongrats! it can get any better than that")
        else:
                print("You got suck by a Venin, and now you are one of them, and now you are stuck in this dark path. Game Over.")
    else:
            print("You got eaten by the Loch Ness Monster. Game Over")

else:
		print("You fall into a hole. You died.\nGame Over")
