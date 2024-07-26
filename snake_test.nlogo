globals [score]

patches-own [seconds-to-live]

to setup
  clear-all
  create-turtles 1 [
    setxy 0 0
    set color red
  ]
  reset-ticks
end

to go
  ; fd 1
  wait 0.1  ; slows down the simulation
  create-fruit
  tick
end

to create-fruit
  every 1 [
    ask patches [
      if count patches with [ pcolor = red ] < 10 [
        set pcolor red
      ]
      
      if pcolor = red and seconds-to-live > 5 [
        set pcolor black
      ]
      
      if pcolor = red [
        set seconds-to-live seconds-to-live + 1
      ]
    ]
  ]
end

to chomp-fruit
  ; still working on this, doesn't actually eat the fruits. turtle problem?
  ask turtles [
    if [pcolor] of patch-here = red [
      set score score + 1
      ask patch-here [ set pcolor black ]
    ]
  ]
end

to move [ new-heading ]
  ask turtles ; probably going to cause a problem with multiple/npc turtles
  [
    set heading new-heading
    fd 1 ; swap comment here and in "go" to make movement continuous
  ]
end
