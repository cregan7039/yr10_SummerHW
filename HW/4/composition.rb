#paste code here
in_thread do
  with_synth "beep"
  2.times do
    play 60
    sleep 0.5
    play 67
    sleep 0.5
    play 60
    sleep 0.5
    play 63
    sleep 0.5
  end
end
    
    
in_thread do
  with_synth "pretty_bell"
  30.times do
    play 49
    sleep 1
  end
end
