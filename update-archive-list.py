import os

docs = list(filter(lambda filename: filename.endswith('html') and filename != 'index.html', os.listdir('./archive/')))

htmllines = []
htmllines.append('''
<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, shrink-to-fit=no">
        <style type="text/css">
            @font-face {
                font-family: 'custom';
                src: url('./milo-primary-subset-rg.woff2');
            } 
            .customisedFont{
                font-family: 'custom';
                font-size:120%;
                line-height: 140%;
            }
        </style>
        <link rel="stylesheet" href="https://arielherself.github.io/espresso-native/mdui-v1.0.2/css/mdui.min.css"/>
        <link rel="shortcut icon" href="https://arielherself.github.io/espresso-native/museum.png" type="image/x-icon">
        <title>Espresso Archive</title>
    </head>
    <body class="mdui-theme-primary-red mdui-color-theme mdui-typo mdui-theme-layout-auto">
        <script>
            document.addEventListener("keydown",listenEnter);
            function listenEnter() {
                if ((event.which || event.keyCode) == 13) {
                    document.getElementById("submit_button").click();
                }
            }
        </script>
        <button mdui-dialog="{target: '#dialog'}" id="hidden_dialog" hidden></button>
        <div class="mdui-appbar mdui-appbar-fixed">
            <div class="mdui-toolbar mdui-color-red-a700">
              <a href="https://github.com/arielherself/espresso-native" class="mdui-btn mdui-btn-icon" mdui-tooltip="{content: 'Project repository', position: 'right'}">
                <i class="mdui-icon material-icons">
                    <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 36 36" enable-background="new 0 0 36 36" xml:space="preserve" class="mdui-icon" style="width: 24px;height:24px;">
                        <path fill-rule="evenodd" clip-rule="evenodd" fill="#ffffff" d="M18,1.4C9,1.4,1.7,8.7,1.7,17.7c0,7.2,4.7,13.3,11.1,15.5c0.8,0.1,1.1-0.4,1.1-0.8c0-0.4,0-1.4,0-2.8c-4.5,1-5.5-2.2-5.5-2.2c-0.7-1.9-1.8-2.4-1.8-2.4c-1.5-1,0.1-1,0.1-1c1.6,0.1,2.5,1.7,2.5,1.7c1.5,2.5,3.8,1.8,4.7,1.4c0.1-1.1,0.6-1.8,1-2.2c-3.6-0.4-7.4-1.8-7.4-8.1c0-1.8,0.6-3.2,1.7-4.4c-0.2-0.4-0.7-2.1,0.2-4.3c0,0,1.4-0.4,4.5,1.7c1.3-0.4,2.7-0.5,4.1-0.5c1.4,0,2.8,0.2,4.1,0.5c3.1-2.1,4.5-1.7,4.5-1.7c0.9,2.2,0.3,3.9,0.2,4.3c1,1.1,1.7,2.6,1.7,4.4c0,6.3-3.8,7.6-7.4,8c0.6,0.5,1.1,1.5,1.1,3c0,2.2,0,3.9,0,4.5c0,0.4,0.3,0.9,1.1,0.8c6.5-2.2,11.1-8.3,11.1-15.5C34.3,8.7,27,1.4,18,1.4z"></path>
                    </svg>
                </i>
              </a>
              <a href="https://te.arielherself.xyz" class="mdui-typo-title" mdui-tooltip="{content: 'Visit the official website', position: 'bottom'}"><b>T</b>he <b>E</b>conomist</a>
              <div class="mdui-toolbar-spacer"></div>
              <a href="javascript:location.reload();" class="mdui-btn mdui-btn-icon" mdui-tooltip="{content: 'Reload (Ctrl+R)', position: 'left'}">
              <i class="mdui-icon material-icons">refresh</i>
              </a>
            </div>
        </div>
        <br><br>
        <div class="mdui-container customisedFont mdui-typo" style="max-width: 768px;">
            <h1 align="center">Espresso Archive</h1>
                <div class="mdui-row">
        <div class="mdui-col-xs-10">
            <div class="mdui-textfield mdui-textfield-expandable">
                <button class="mdui-textfield-icon mdui-btn mdui-btn-icon" mdui-tooltip="{content: 'Go to article...'}" onclick="document.getElementById(`submit_button`).hidden=false;">
                  <i class="mdui-icon material-icons">search</i>
                </button>
                <input class="mdui-textfield-input" type="text" placeholder="YYYY-MM-DD(Back up to 2022-07-24)" id="targ" />
                <button class="mdui-textfield-close mdui-btn mdui-btn-icon" onclick="document.getElementById(`submit_button`).hidden=true;">
                  <i class="mdui-icon material-icons" mdui-tooltip="{content: 'Cancel'}">close</i>
                </button>
              </div>    
        </div>
        <div class="mdui-col-xs-2">
            <button class="mdui-btn mdui-color-red-a700" id="submit_button" hidden onclick="window.open(document.getElementById(`targ`).value+`.html`);">Go</button>
        </div>
    </div><hr>
            <div class="mdui-table-fluid">
                <table class="mdui-table mdui-table-hoverable">
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>Date</th>
                      <th>Link</th>
                    </tr>
                  </thead>
                  <tbody>
''')

for i, each in enumerate(sorted(docs, reverse=True)):
    htmllines.append(f'''
<tr>
<td>{i+1}</td>
<td>{each[:-5]}</td>
<td><a href="https://arielherself.github.io/espresso-native/archive/{each[:-5]}.html">https://arielherself.github.io/espresso-native/archive/{each[:-5]}.html</a></td>
''')

htmllines.append('''
</tbody>
</table>
</div>
        </div>


<script src="https://arielherself.github.io/espresso-native/mdui-v1.0.2/js/mdui.min.js"></script>
</body>
</html>
''')

with open('./archive/index.html', 'w', encoding='utf8') as fil:
    print(*htmllines, sep='\n', file=fil)
