# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:54:13 2019

@author: Administrator
"""
#MON 是 Max Object Number的简写
#dictlist=[{'entity1': '本车', 'entity2': '树林', 'direction': '右侧', 'distance': '55'}, {'entity1': '道路', 'entity2': '房屋', 'direction': '左侧', 'distance': '118'},{'entity1': '本车', 'entity2': '加油', 'direction': '左侧', 'distance': '7'},]
order = {'link':0,
        'forest':0,
         'house':0,
         'mount':0,
         'plate':0,
         'object':56
         }

def cast_dict(dic):
    se = ''
    if dic['entity2'] == '森林' or dic['entity2'] == '树林':
        se += 'Link.'+str(order['link'])+'.TreeStrip.'+str(order['forest'])+'.ID = ' + str(order['object']) + '\n'
        startx = float(dic['distance'])
        normal_forest_length = 20
        endx = float(dic['distance']) + normal_forest_length
        default_offset = 5
        if dic['direction'] == '右侧':
            default_offset = -30
        se += 'Link.'+str(order['link'])+'.TreeStrip.'+str(order['forest'])+' = '+ str(startx) +' 0 '+ str(endx) +' 0 '+str(default_offset)+' 1 10 5 1 1 0.5 0.5 \n'
        order['object'] += 1 
        order['forest'] += 1
        return se
    elif dic['entity2'] == '房屋':
        se += 'Link.'+str(order['link'])+'.GeoObject.'+str(order['house'])+'.ID = ' + str(order['object']) + '\n'
        startx = float(dic['distance'])
        endx = float(dic['distance'])
        default_offset = 30
        if dic['direction'] == '右侧':
            default_offset = -30
        se += 'Link.'+str(order['link'])+'.GeoObject.'+str(order['house'])+' = '+str(startx)+' 0 '+str(endx)+' 0 '+str(default_offset)+' 100 0 0 0 0 0 1 1 1 0 3D/Buildings/FamilyHouse_00_1.mobj \n'
        se += 'Link.'+str(order['link'])+'.GeoObject.'+str(order['house'])+'.SensorBBox = 1 0 18.42 -10.8 9.7 0 9.1 \n'
        #Link.0.GeoObject.0.ID = 56
        #Link.0.GeoObject.0 = 154.342 0 154.342 0 -35.132 100 0 0 0 0 0 1 1 1 0 3D/Buildings/FamilyHouse_00_1.mobj
        #Link.0.GeoObject.0.SensorBBox = 1 0 18.42 -10.8 9.7 0 9.1
        order['object'] += 1
        order['house'] += 1
        return se
    elif dic['entity2'] == '加油站':
        se += 'Link.'+str(order['link'])+'.GeoObject.'+str(order['house'])+'.ID = ' + str(order['object']) + '\n'
        startx = float(dic['distance'])
        endx = float(dic['distance'])
        default_offset = 40
        if dic['direction'] == '右侧':
            default_offset = -60
        se += 'Link.'+str(order['link'])+'.GeoObject.'+str(order['house'])+' = '+str(startx)+' 0 '+str(endx)+' 0 '+str(default_offset)+' 100 0 0 0 0 0 1 1 1 0 3D/Buildings/GasStation_01.mobj \n'
        se += 'Link.'+str(order['link'])+'.GeoObject.'+str(order['house'])+'.SensorBBox = 1 0 18.42 -10.8 9.7 0 9.1 \n'
        #Link.0.GeoObject.0.ID = 56
        #Link.0.GeoObject.0 = 154.342 0 154.342 0 -35.132 100 0 0 0 0 0 1 1 1 0 3D/Buildings/FamilyHouse_00_1.mobj
        #Link.0.GeoObject.0.SensorBBox = 1 0 18.42 -10.8 9.7 0 9.1
        order['object'] += 1
        order['house'] += 1
        return se
    elif dic['entity2'] == '商店':
        se += 'Link.'+str(order['link'])+'.GeoObject.'+str(order['house'])+'.ID = ' + str(order['object']) + '\n'
        startx = float(dic['distance'])
        endx = float(dic['distance'])
        default_offset = 40
        if dic['direction'] == '右侧':
            default_offset = -60
        se += 'Link.'+str(order['link'])+'.GeoObject.'+str(order['house'])+' = '+str(startx)+' 0 '+str(endx)+' 0 '+str(default_offset)+' 100 0 0 0 0 0 1 1 1 0 3D/Buildings/Kiosk_02_1.mobj \n'
        se += 'Link.'+str(order['link'])+'.GeoObject.'+str(order['house'])+'.SensorBBox = 1 0 18.42 -10.8 9.7 0 9.1 \n'
        order['object'] += 1
        order['house'] += 1
        return se
    elif dic['entity2'] == '办公楼':
        se += 'Link.'+str(order['link'])+'.GeoObject.'+str(order['house'])+'.ID = ' + str(order['object']) + '\n'
        startx = float(dic['distance'])
        endx = float(dic['distance'])
        default_offset = 40
        if dic['direction'] == '右侧':
            default_offset = -60
        se += 'Link.'+str(order['link'])+'.GeoObject.'+str(order['house'])+' = '+str(startx)+' 0 '+str(endx)+' 0 '+str(default_offset)+' 100 0 0 0 0 0 1 1 1 0 3D/Buildings/Office_01.mobj \n'
        se += 'Link.'+str(order['link'])+'.GeoObject.'+str(order['house'])+'.SensorBBox = 1 0 18.42 -10.8 9.7 0 9.1 \n'
        order['object'] += 1
        order['house'] += 1
        return se    
    elif dic['entity2'] == '办公楼':
        se += 'Link.'+str(order['link'])+'.GeoObject.'+str(order['house'])+'.ID = ' + str(order['object']) + '\n'
        startx = float(dic['distance'])
        endx = float(dic['distance'])
        default_offset = 40
        if dic['direction'] == '右侧':
            default_offset = -60
        se += 'Link.'+str(order['link'])+'.GeoObject.'+str(order['house'])+' = '+str(startx)+' 0 '+str(endx)+' 0 '+str(default_offset)+' 100 0 0 0 0 0 1 1 1 0 3D/Buildings/Office_01.mobj \n'
        se += 'Link.'+str(order['link'])+'.GeoObject.'+str(order['house'])+'.SensorBBox = 1 0 18.42 -10.8 9.7 0 9.1 \n'
        order['object'] += 1
        order['house'] += 1
        return se       
    elif dic['entity2'] == '车站' or dic['entity2'] == '地铁站':
        se += 'Link.'+str(order['link'])+'.GeoObject.'+str(order['house'])+'.ID = ' + str(order['object']) + '\n'
        startx = float(dic['distance'])
        endx = float(dic['distance'])
        default_offset = 40
        if dic['direction'] == '右侧':
            default_offset = -60
        se += 'Link.'+str(order['link'])+'.GeoObject.'+str(order['house'])+' = '+str(startx)+' 0 '+str(endx)+' 0 '+str(default_offset)+' 100 0 0 0 0 0 1 1 1 0 3D/Buildings/SubwayEntrance_03.mobj \n'
        se += 'Link.'+str(order['link'])+'.GeoObject.'+str(order['house'])+'.SensorBBox = 1 0 18.42 -10.8 9.7 0 9.1 \n'
        order['object'] += 1
        order['house'] += 1
        return se     
    elif dic['entity2'] == '广告牌':
        default_offset = 20
        startx = float(dic['distance'])
        if dic['direction'] == '右侧':
            default_offset = -20
        se += 'Link.'+str(order['link'])+'.GeoObject.'+str(order['house'])+'.ID = ' + str(order['object']) + '\n'
        se += 'Link.'+str(order['link'])+'.SignPlate.'+str(order['plate'])+' = '+str(startx)+' 0 '+str(default_offset)+' 100 1 4 0 1 3 \"\" \n'
        se += 'Link.'+str(order['link'])+'.SignPlate.'+str(order['plate'])+'.Material.0 = Textures/IPG/Logo_IPG_01.jpg 0 0 0 0 0 0 1 1 0 0 0 \n'
        #Link.0.SignPlate.0.ID = 9
        #Link.0.SignPlate.0 = 126.947 0 -23.336 100 1 4 0 1 3 ""
        #Link.0.SignPlate.0.Material.0 = Textures/IPG/Logo_IPG_01.jpg 0 0 0 0 0 0 1 1 0 0 0
        order['house'] += 1
        order['object'] += 1
        order['plate'] += 1
        return se
    elif dic['entity2'] == '红绿灯' or dic['entity2'] == '信号灯':
        default_offset = 5
        site = 1
        startx = float(dic['distance'])
        facing = -1
        if dic['direction'] == '右侧':
            default_offset = -5
            site = -1
            facing = 1
        se += 'Link.'+str(order['link'])+'.Mount.'+str(order['mount'])+'.ID = '+ str(order['object']) +' \n'
        se += 'Link.'+str(order['link'])+'.Mount.'+str(order['mount'])+' = '+str(startx)+' 0 '+str(default_offset)+' '+str(site)+' 1 5 0 0 0 \n'
        order['object'] += 1
        se += 'Link.'+str(order['link'])+'.Mount.'+str(order['mount'])+'.0.ID = '+ str(order['object']) +' \n'
        se += 'Link.'+str(order['link'])+'.Mount.'+str(order['mount'])+'.0 = 1 2.5 0 0 0 0 0 TL000 -1 '+str(facing)+' 0 "" 1 1 0 15 3 15 3 \n'
        #Link.0.Mount.0.ID = 2
        #Link.0.Mount.0 = 35.631 0 -5.399 -1 1 5 0 0 0
        #Link.0.Mount.0.0.ID = 3
        #Link.0.Mount.0.0 = 1 2.5 0 0 0 0 0 TL000 -1 1 0 "" 1 1 0 15 3 15 3
        order['object'] += 1
        order['mount'] += 1
        return se
    elif dic['entity2'] == '标志牌' or dic['entity2'] == '交通标志':
        default_offset = 5
        site = 1
        startx = float(dic['distance'])
        facing = -1
        relevance_to_mount = -1
        if dic['direction'] == '右侧':
            default_offset = -5
            site = -1
            facing = 1
            relevance_to_mount = 1            
        se += 'Link.'+str(order['link'])+'.Mount.'+str(order['mount'])+'.ID = '+ str(order['object']) +' \n'
        se += 'Link.'+str(order['link'])+'.Mount.'+str(order['mount'])+' = '+str(startx)+' 0 '+str(default_offset)+' '+str(site)+' 1 5 0 0 0 \n'
        order['object'] += 1
        se += 'Link.'+str(order['link'])+'.Mount.'+str(order['mount'])+'.0.ID = '+ str(order['object']) +' \n'
        se += 'Link.'+str(order['link'])+'.Mount.'+str(order['mount'])+'.0 = 0 2 0 0 0 0 0 -1 '+str(relevance_to_mount)+' 1 Stop M "" 0 0 0 - - "" 0 0 0 - - "" 0 0 0 \n'
        se += 'Link.'+str(order['link'])+'.Mount.'+str(order['mount'])+'.0.Size = 0.899999976158142 0.899999976158142 \n'
        order['object'] += 1
        order['mount'] += 1
        #Link.0.Mount.2.ID = 9
        #Link.0.Mount.2 = 66.864 0 -7.106 -1 1 1 0 0 0
        #Link.0.Mount.2.0.ID = 19
        #Link.0.Mount.2.0 = 0 2 0 0 0 0 0 -1 1 1 Stop M "" 0 0 0 - - "" 0 0 0 - - "" 0 0 0
        #Link.0.Mount.2.0.Size = 0.899999976158142 0.899999976158142
        return se
    else: 
        return se
        
def dict2rd5(dic_list):

    
    with open('senario.rd5', 'w') as f:
        s = u'''#INFOFILE1.1 - Do not remove this line!
FileIdent = IPGRoad 7.0
FileCreator = CarMaker 7.1
LibVersion = 7.1
Country = DEU
nLinks = 1
nJunctions = 0
nObjects = 56
nRoutes = 0
RoadNetworkLength = 200
BBox = -10 205 -17 17 -11 11
RST.Unit = kmh
RST = 50 100 130 30 70 30 0 -1
Movie = 0.2 1 0.01 1.5 1.5 1 1
Movie.BgGeoFName =
Movie.BgGeoOptions =
Movie.TerrainFName =
PathMode = -1
Link.0.ID = 0
Link.0.Junctions = -2 -1 -2 -1
Link.0.Node0 = 0 0 0 -0
Link.0.RST = countryroad
Link.0.RL.ID = 1
Link.0.Seg.0.ID = 5
Link.0.Seg.0.Type = Straight
Link.0.Seg.0.Param = 200 0 0 0 0 0 0 0
Link.0.LaneSection.0.ID = 6
Link.0.LaneSection.0.Start = 0
Link.0.LaneSection.0.LaneL.0.ID = 7
Link.0.LaneSection.0.LaneL.0 = 0 3.5 3.5 0 0 0 0
Link.0.LaneSection.0.LaneL.0.ARP = 10 11 12 13 14 15
Link.0.LaneSection.0.LaneL.0.RoadMarking.0.ID = 17
Link.0.LaneSection.0.LaneL.0.RoadMarking.0 = 0 0 0 1 0 1 0.15 0 1 0 0 2 4 1 1 0 ""
Link.0.LaneSection.0.LaneL.0.RoadMarking.0.Material.0 = 1.0,1.0,1.0 0 0 0 0 0 0 0 0 0 0 0
Link.0.LaneSection.0.LaneL.1.ID = 18
Link.0.LaneSection.0.LaneL.1 = 0 1 1 4 0 0 0
Link.0.LaneSection.0.LaneL.1.ARP = 21 22 23 24 25 26
Link.0.LaneSection.0.LaneL.2.ID = 28
Link.0.LaneSection.0.LaneL.2 = 0 2.5 2.5 5 0 0 0
Link.0.LaneSection.0.LaneR.0.ID = 31
Link.0.LaneSection.0.LaneR.0 = 0 3.5 3.5 0 0 0 0
Link.0.LaneSection.0.LaneR.0.ARP = 34 35 36 37 38 39
Link.0.LaneSection.0.LaneR.0.RoadMarking.0.ID = 41
Link.0.LaneSection.0.LaneR.0.RoadMarking.0 = 0 0 0 1 0 -1 0.15 0 1 0 0 2 4 1 1 0 ""
Link.0.LaneSection.0.LaneR.0.RoadMarking.0.Material.0 = 1.0,1.0,1.0 0 0 0 0 0 0 0 0 0 0 0
Link.0.LaneSection.0.LaneR.1.ID = 42
Link.0.LaneSection.0.LaneR.1 = 0 1 1 4 0 0 0
Link.0.LaneSection.0.LaneR.1.ARP = 45 46 47 48 49 50
Link.0.LaneSection.0.LaneR.2.ID = 52
Link.0.LaneSection.0.LaneR.2 = 0 2.5 2.5 5 0 0 0
Link.0.LaneSection.0.RoadMarking.0.ID = 55
Link.0.LaneSection.0.RoadMarking.0 = 0 0 0 1 0 0 0.15 0 2 0 0 2 4 1 1 0 ""
Link.0.LaneSection.0.RoadMarking.0.Material.0 = 1.0,1.0,1.0 0 0 0 0 0 0 0 0 0 0 0
LanePath.0 = 16 7 2 10 0.1 0.1
LanePath.1 = 27 18 0.25 10 0.1 0.1
LanePath.2 = 40 31 2 10 0.1 0.1
LanePath.3 = 51 42 0.25 10 0.1 0.1 \n'''
        for each_dic in dic_list:
            
            s += str(cast_dict(each_dic))

        s+='MaxUsedObjId = '+ str(order['object']-1)
        #print(s)
        f.write(s)
        f.close()
    
#dict2rd5(dictlist)