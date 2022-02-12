# auto3Dprintcam
## Update 1: 12 feb 2022
I needed to adjust the original install instructions to change from libjpeg8-dev to libjpeg9-dev in this part: 
```
sudo apt-get install build-essential libjpeg9-ev imagemagick libv4l-dev git cmake uvcdynctrl
```
## Main info
I wanted to monitor my 3D-printer automated with a simple cam connected to an RPi so I got the hardware and printed 
some cases for it and did some coding.

This program starts a webcam on my 3D-printer when the light/printer turns on and stops when it is turned of.

I have used the rpi-mjpg-streamer by meinside (https://github.com/meinside/rpi-mjpg-streamer) and installed according to 
his description and it works like a charm.

I am using an wide-angle rpi-cam like this https://www.amazon.co.uk/Raspberry-Wide-Angle-Fish-Eye-Camera/dp/B00N1YJKFS
plus an photo resistor/light sensor modul for Raspberry Pis found in this example:
http://www.uugear.com/portfolio/using-light-sensor-module-with-raspberry-pi/

The housing is a mix of different housing for the parts plus a part for having it all hanging on my 3D printer.

The startcam.sh and stopcam.sh are basically the same code as in Liams example, I have just added my own login and 
a different port for the webpage. 

Then I wrote the start_light_sensor.py to sense the light of the printer and start the startcam.sh when printer is turned on 
(the light on it turns on) and when the printer is turned of (and so will the light) trigger the stopcam.sh

I added som info when it starts and stops plus some logic for not allways polling for the sensor, it just kicks of when 
there is a change in the light sensor.

When printer is on:
<img src="https://lh3.googleusercontent.com/5Em_1LcUUTc5ShWbAxS-tmmlcLZ-dyHTSafWTviRcWYmaCM5NoU-iopV6Ue_pG0yPIisSI-2A4iOACS5Zir82gWW7i9qhQct81HXhtE2f3g4m-_wNi_U6MCXrc2ZrPOSybczvSLYd9tTYpzyfgNDrhI4sxbFgke-cmu6bOToA_ylF6cpDAeMs_TBGTM_MFG1nv0_ejDAZPhn7s1XmWqLwk7K0IgEQypgCHm-syOrMzEp3EK00db3L_bpNJgFTc2zNEV5YM72YuF7y3iSyy7eRCVadBa-m1UgdukfWsO4iz0nhs_otx4X0E8rfNsnenM24xNhhDLEjDHY38it-_ZXTQ-qomRNJ_740pMUiK6VJKKts9jZ3G45XqWfYJqrwsG7IIWQjaRkNk-cmtWrOjVxnJXWjxKTlS1pHUV2IyBTENcVAwA3YDfFbuQe6wcxbL0U7vgdZ31AfDascax_5BpcsvgxCsw3ONYdjvgox-9kKcnWkrdlTzdREbEBn-Awq6x8LltWebGd68ViZ-uy3ymyv-H3Ss1cd5v-C7sd2MuyOjz0P2ZOdUR139OYT2GDd455bL1oXqOWAxmDzHV_4S19urYQWJnd7E2YzUNFn3ns3VZWDSs0HzsK8uUA1KI9fTzO4i_dFNc9sEtlKleTLJTMJMiHIFfXbtJ0NsMGwW84ZIcysOCbbcy0jCtIKngi4hAcflmFEMiBb8gaJNqSCuOHY6HEjQ=w1920-h934-no">

When printer is off:
<img src="https://lh3.googleusercontent.com/XcTSSLjuAyInUdLa5F2zmk2wizRg9N33bQRF6kibw2t0TgLlJ7SUnvuks7O9xfnCkBHOp_P64r_T6WzcfKuoQYDlkTEimsgKhw8VVkIvC75nbiV06s9qC6Brum_pCxmpJbMnhNhd6JvHHPj3x4JINKNyLlH-gjB38lZ2MTBHSHv3IKINLxqrHvMM_xnoVMGg1mUOh4_-scVSyXQPwgl2N_nuf4zu_6UYuT8XsSqN1aLEq4yiKttFGuYCUvDdoqSJ2ViTGTj7AcwSoi7mEysqRm8-HLfTpV77S0Az5vWG9ryPTuWbAtj_A8fVKHztNqXJgP2H_qPGSxAdAChB2RU8ifKshHxatMPKcA8gHOPrsl8yJdAXhi9UkZS-AQbeYVux8WKNlim9W1wH0ri4ZE1cmV9USoiP6-rC3H0w1Yv3MB9gG4CTydjk4RQrCyqq5PY7VxN_L_3f3Kt2evk7giHRfY-Y4H9nutcr__DyPTm7dFd3dUcjA1Ev09qoPe79bCpLiG3KZB5FHmujVuc_BEtePUT3rUxnCCMnwvBuNjeaEvFiEYye5pxVj3_Vm8CySFocVOfV2iY1YvmB52U1kCojjYn9gNPfvRuEFlUgc2RIjKrJTTOgLIregfntvC_2l6jEXhZxxgkvl669A8D79WgxjM9rv6hnuaSaA_dlSKOaNuEOrfHRQ2TS80lfr3Fc--EyT_OUwkTkVgfT82vsAtqBKLJ8jQ=w1920-h934-no">

Pic on the printed cases for the hardware:
<img src="https://lh3.googleusercontent.com/3X6HrI7hx3ND-n5r0y1wq9fAkVaolU-2HY552jkb5f9TQck4dbhrOkhjYsZpCZr7ks6FkXYVxXyDSaSxDWA3UNeCrQgv1iThnRdatnrRoMqHGjhK_lOB0XRqb8BYeh3efiPv9tWVDa1zIj3zjJy3yMojHz6e6D1gSiAEwh-r3gndKO05CfgymlV-4gAzIILbg3EcXWqXB6aYduGRD_RH-0hVxdcGbaSyVUTYGhQmziksWRUx9tASeDlUAUprbuQe-dRwRD0lmwAipvhgIF2QtsVVrQ0Dfpj6Socq3X5C80joJvYLuefNV-xUCCbSpE0NOOK2jIWy7bdIPOLBDpMaw9pk1-5gxgHrDXBCAghsspfpnuCa0RiX4c5n5nII-dOC6UVeg43WJnPFM96gWXJR280MT-vdsab67CQewLCik2pnzLH6S7zaulHrZL1hWvdaHIkZXCDe5rsbBdf5qxdmg3hi-UoEi49bobdYd3Vk3PdbDwptcDpS06QHSYpo-_nbvj503KAi_U18YGi2YyTOt00vSX0-A9-x5CoT5CunpQQEqFLaV7Qe2SuKFx-GL560ZIPRl1xLvj0ERCXAm389cc_jPFciwiqq7dAOntVKcvJzdV0EMNwW6EgESXr19ywIbC8o8KxYrjeB4UWG2WhUg2gO-9Z_GYhCNh9aeHkBOerw_oAXg2Iq--m74WRdc6F8X_kcbuD4G_KG29fNdbA9HUcF3w=w1695-h947-no">
<img src="https://lh3.googleusercontent.com/pB4yY9gT357FtjVKjqhwuyLZ_TTRqDsYuLTFq9ZsGiH5r3L3LtRQxH4Fr9WKbhFYgN-IwYDXh78qpCDeUWPcomx8VY4kjjnfwCWgrBx5VKiosGGwj174iW9rBU_vSHgypii9EDwiI_H3tWhIZ9rbDAKorJnIVwWQq6kR-pnQZHs8Le47cEq_jJBZuscD1K5q3_GmHnXMIozrDUOIfYJ9RHSj8ZmBrHrT7BIO1df617N6WXbke-jbFZ5URj8RVnCvPi2xcrFLTVzcIy7dA5F2J45t_Oy1BuoKwwVxArmHGX69vLznM-F_MMnc2tibfK8g2DSQ5scIp1LoPFLQLM3sosXF6DPYYJH6iV9ma2ngBeGZuQaC9soC_4ad-CBCiWjvXIXPsmTPFCgekRVZkv3j0RsG-o639AJwN-acO80l6D1zxgqrnrcnJSJBdreyzre2QwwDL6LSKhCbC7nbamarJNA522AsVGsWQVISsMYSruUbk36GTrP4Rne9MvZvkPEv3Jcjjn4Bsf49hFy_WtMLKi9UUd3bwhidnzVAIQF1w7sZwdu81wYa_gTKN_Wt1RIWlbtBQHfhlZ8Yz8-iNN4keFYJ428HLo2b6Omir2vbwbMz1IfJ0SIaMTyA5QnwpWaDUKWyJOifbHRJolLG4zYx7uJ5Qp0t8Lt7ooYtotnxMVWf6gm7zLfNJXMUsRsEXU-4x5VhEf8zVeG8wu2b9FmAX12kqA=w530-h948-no">
