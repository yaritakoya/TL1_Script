import bpy

bl_info={
    "name":"レベルエディタ",
    "author":"koya yarita",
    "version":(1,0),
    "blender":(3,3,1),
    "location":"",
    "description":"レベルエディタ",
    "warning":"",
    "wiki_url":"",
    "category":"Object"
}

#アドオン有効化時コールバック
def register():
    print("レベルエディタが有効化されました")

#アドオン無効化時コールバック
def unregister():
    print("レベルエディタが無効化されました")