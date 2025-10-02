# Version conflict

https://github.com/nanophysics/compact_2012/blob/master/requirements.txt#L14-L16

https://github.com/nanophysics/heater_thermometrie_2021/blob/main/requirements.txt#L13-L14

## Projects using mpfshell2

```
grep -r "^mpfshell2" --include="requirements.txt" .
```

<!--
./ETH-Compact/git_compact_2012/requirements.txt:mpfshell2>=100.9.17
./ETH-Elias/software/requirements.txt:mpfshell2 >= 100.9.10
./ETH-humidity_controller_2022/requirements.txt:mpfshell2>=100.9.17
./ETH-insert_2019/git/heater_thermometrie_2021/software_vorgaben/software/requirements.txt:mpfshell2        
./ETH-insert_2019/labber_drivers/heater_thermometrie_2021/requirements.txt:mpfshell2>=100.9.17
./ETH-labber_ad_low_noise_float_2023/gits/compact_2012/requirements.txt:mpfshell2==100.9.17
./ETH-scanner_pyb/software/requirements.txt:mpfshell2 >= 100.9.10
./ETH_gnd_loop_alert_2020_git/software/requirements.txt:mpfshell2
-->

* https://github.com/nanophysics/compact_2012/blob/master/requirements.txt#L14-L16
* https://github.com/nanophysics/heater_thermometrie_2021/blob/main/requirements.txt#L13-L14
* https://github.com/nanophysics/humidity_controller_2022/blob/main/requirements.txt#L1
* https://github.com/nanophysics/labber_ad_low_noise_float_2023/blob/main/requirement_stimuli.txt#L1-L3
* https://github.com/petermaerki/critical_current_time1_elias_2021_git/blob/main/software/requirements.txt#L1
* https://github.com/petermaerki/gnd_loop_alert_2020_git/blob/master/software/requirements.txt#L1
* https://github.com/petermaerki/scanner_pyb/blob/master/software/requirements.txt#L1

## Goal

mpfshell2 should be adapted as such that the newest version works again against compact_2012 and heater_thermometrie_2021.
