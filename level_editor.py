import bpy

bl_info = {
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

#メニュー項目描画
def draw_menu_manual(self,context):
    #self:呼び出し元のクラスインスタンス。C++でいうthisポインタ
    #context:カーソルを合わせた時のポップアップのカスタマイズに使用

    #トップバーの「エディターメニュー」に項目（オペレータ）を追加
    self.layout.operator("wm.url_open_preset",text="Manual",icon="HELP")

# トップバーの拡張メニュー
class TOPBAR_MT_my_menu(bpy.types.Menu):

    # Blenderがクラスを識別するための固有の文字列
    bl_idname = "TOPBAR_MT_my_menu"

    # メニューのラベルとして表示される文字列
    bl_label = "MyMenu"

    # 警告表示用の文字列
    bl_description = "拡張メニュー by " + bl_info["author"]

    # サブメニューの描画
    def draw(self, context):

        # トップバーの「エディタメニュー」に項目(オペレータ)を追加
        self.layout.operator(
            "wm.url_open_preset",
            text="Manual",
            icon="HELP"
        )

# 既存のメニューにサブメニューを追加
def submenu(self, context):

    # ID指定でサブメニューを追加
    self.layout.menu(TOPBAR_MT_my_menu.bl_idname)

#Blenderに登録するクラスリスト
classes = (
    TOPBAR_MT_my_menu,
)

#アドオン有効化時コールバック
def register():
    #Blenderにクラスを登録
    for cls in classes:
        bpy.utils.register_class(cls)

    #メニュー項目を追加
    bpy.types.TOPBAR_MT_editor_menus.append(submenu)
    
    print("レベルエディタが有効化されました")

#アドオン無効化時コールバック
def unregister():
    #メニューから項目を削除
    bpy.types.TOPBAR_MT_editor_menus.remove(submenu)

    #Blenderからクラスを削除
    for cls in classes:
        bpy.utils.unregister_class(cls)

    print("レベルエディタが無効化されました")