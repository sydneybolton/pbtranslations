(DATPenSet()
    .append(DATPen()
        .tag("parameter-edges")
        .moveTo((0.0, 620.0))
        .lineTo((126.0, 620.0))
        .endPath()
        .moveTo((146.0, 314.0))
        .lineTo((614.0, 314.0))
        .endPath()
        .moveTo((634.0, 620.0))
        .lineTo((760.0, 620.0))
        .endPath()
        .moveTo((126.0, 188.0))
        .lineTo((380.0, 188.0))
        .endPath()
        .moveTo((380.0, 188.0))
        .lineTo((634.0, 188.0))
        .endPath()
        .moveTo((532.0, 60.0))
        .lineTo((532.0, 128.0))
        .endPath()
        .moveTo((608.0, 60.0))
        .lineTo((608.0, 128.0))
        .endPath()
        .moveTo((684.0, 60.0))
        .lineTo((684.0, 128.0))
        .endPath()
        .moveTo((126.0, 128.0))
        .lineTo((126.0, 676.0))
        .endPath()
        .moveTo((634.0, 246.0))
        .lineTo((634.0, 676.0))
        .endPath()
        .moveTo((126.0, 246.0))
        .lineTo((380.0, 246.0))
        .endPath()
        .moveTo((380.0, 128.0))
        .lineTo((380.0, 246.0))
        .endPath()
        .moveTo((380.0, 246.0))
        .lineTo((634.0, 246.0))
        .endPath()
        .moveTo((634.0, 128.0))
        .lineTo((634.0, 246.0))
        .endPath()
        .moveTo((1004.0, 608.0))
        .lineTo((1004.0, 676.0))
        .endPath()
        .moveTo((1304.0, 608.0))
        .lineTo((1304.0, 676.0))
        .endPath()
        .moveTo((884.0, 608.0))
        .lineTo((1444.0, 608.0))
        .endPath()
        .moveTo((884.0, 556.0))
        .lineTo((1444.0, 556.0))
        .endPath()
        .f(bw(0.0, 0.0))
        .s(bw(0.5))
        .sw(3))
    .append(DATPen()
        .tag("clump-edges")
        .moveTo((0, 60))
        .lineTo((760, 60))
        .endPath()
        .moveTo((0.0, 128.0))
        .lineTo((760.0, 128.0))
        .endPath()
        .f(bw(0.0, 0.0))
        .s(bw(0.25))
        .sw(5))
    .append(DATPen()
        .tag("sidebar")
        .moveTo((760, 0))
        .lineTo((884, 0))
        .lineTo((884, 676))
        .lineTo((760, 676))
        .closePath()
        .f(bw(0.5)))
    .append(DATPen()
        .tag("advbar")
        .moveTo((884, 0))
        .lineTo((1444, 0))
        .lineTo((1444, 60))
        .lineTo((884, 60))
        .closePath()
        .f(bw(0.75)))
    .append(DATPenSet()
        .tag("labels")
        .append(DATPen()
            .tag("param")
            .add_data({'ts': ['ParamLabel/text', 'Bias', None]})
            .moveTo((132.0, 192.0))
            .lineTo((200.0, 192.0))
            .lineTo((200.0, 250.0))
            .lineTo((132.0, 250.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .tag("param")
            .add_data({'ts': ['ParamLabel/text', 'Noise', None]})
            .moveTo((306.0, 132.0))
            .lineTo((374.0, 132.0))
            .lineTo((374.0, 192.0))
            .lineTo((306.0, 192.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .tag("param")
            .add_data({'ts': ['ParamLabel/text', 'Bias', None]})
            .moveTo((386.0, 192.0))
            .lineTo((454.0, 192.0))
            .lineTo((454.0, 250.0))
            .lineTo((386.0, 250.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .tag("param")
            .add_data({'ts': ['ParamLabel/text', 'Noise', None]})
            .moveTo((560.0, 132.0))
            .lineTo((628.0, 132.0))
            .lineTo((628.0, 192.0))
            .lineTo((560.0, 192.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .tag("param")
            .add_data({'ts': ['ParamLabel/text', 'dry', None]})
            .moveTo((6, 60))
            .lineTo((134.0, 60.0))
            .lineTo((134.0, 128.0))
            .lineTo((6.0, 128.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .tag("clump")
            .add_data({'ts': ['ClumpLabel/text', 'I', None]})
            .moveTo((14.0, 620.0))
            .lineTo((112.0, 620.0))
            .lineTo((112.0, 676.0))
            .lineTo((14.0, 676.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .tag("clump")
            .add_data({'ts': ['ClumpLabel/text', 'O', None]})
            .moveTo((648.0, 620.0))
            .lineTo((746.0, 620.0))
            .lineTo((746.0, 676.0))
            .lineTo((648.0, 676.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .tag("clump")
            .add_data({'ts': ['ClumpLabel/text', 'FILTER', None]})
            .moveTo((1018.0, 608.0))
            .lineTo((1290.0, 608.0))
            .lineTo((1290.0, 676.0))
            .lineTo((1018.0, 676.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .tag("clump")
            .add_data({'ts': ['ClumpLabel/text', 'Tilt', None]})
            .moveTo((898.0, 556.0))
            .lineTo((970.0, 556.0))
            .lineTo((970.0, 608.0))
            .lineTo((898.0, 608.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPenSet()
            .tag("options")
            .add_data({'initialValue': 0, 'string_count': 8, 'shows_all_strings': False})
            .append(DATPen()
                .tag("value")
                .add_data({'ts': ['Parameter/option', 'Tube X', 'TubeMode'], 'value': 0})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'ts': ['Parameter/option', 'Tube Y', 'TubeMode'], 'value': 1})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'ts': ['Parameter/option', 'Tube Z', 'TubeMode'], 'value': 2})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'us': 'Reserved 1', 'value': 3})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'us': 'Reserved 2', 'value': 4})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'us': 'Reserved 3', 'value': 5})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'us': 'Reserved 4', 'value': 6})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'us': 'Reserved 5', 'value': 7})
                .moveTo((158.0, 258.0))
                .lineTo((348.0, 258.0))
                .lineTo((348.0, 302.0))
                .lineTo((158.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .tag("options")
            .add_data({'initialValue': 0, 'string_count': 8, 'shows_all_strings': False})
            .append(DATPen()
                .tag("value")
                .add_data({'ts': ['Parameter/option', '2 Track Hi', 'TapeMode'], 'value': 0})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'ts': ['Parameter/option', '2 Track Lo', 'TapeMode'], 'value': 1})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'ts': ['Parameter/option', 'C90 Hi', 'TapeMode'], 'value': 2})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'ts': ['Parameter/option', 'C90 Lo', 'TapeMode'], 'value': 3})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'us': 'Reserved 1', 'value': 4})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'us': 'Reserved 2', 'value': 5})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'us': 'Reserved 3', 'value': 6})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'us': 'Reserved 4', 'value': 7})
                .moveTo((412.0, 258.0))
                .lineTo((602.0, 258.0))
                .lineTo((602.0, 302.0))
                .lineTo((412.0, 302.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .tag("options")
            .add_data({'initialValue': 1, 'string_count': 1, 'shows_all_strings': False})
            .append(DATPen()
                .tag("value")
                .add_data({'us': 'TU', 'value': 0})
                .moveTo((538.0, 66.0))
                .lineTo((602.0, 66.0))
                .lineTo((602.0, 122.0))
                .lineTo((538.0, 122.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'us': 'TU', 'value': 1})
                .moveTo((538.0, 66.0))
                .lineTo((602.0, 66.0))
                .lineTo((602.0, 122.0))
                .lineTo((538.0, 122.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .tag("options")
            .add_data({'initialValue': 1, 'string_count': 1, 'shows_all_strings': False})
            .append(DATPen()
                .tag("value")
                .add_data({'us': 'PE', 'value': 0})
                .moveTo((614.0, 66.0))
                .lineTo((678.0, 66.0))
                .lineTo((678.0, 122.0))
                .lineTo((614.0, 122.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'us': 'PE', 'value': 1})
                .moveTo((614.0, 66.0))
                .lineTo((678.0, 66.0))
                .lineTo((678.0, 122.0))
                .lineTo((614.0, 122.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .tag("options")
            .add_data({'initialValue': 1, 'string_count': 1, 'shows_all_strings': False})
            .append(DATPen()
                .tag("value")
                .add_data({'us': 'FLT', 'value': 0})
                .moveTo((690.0, 66.0))
                .lineTo((754.0, 66.0))
                .lineTo((754.0, 122.0))
                .lineTo((690.0, 122.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'us': 'FLT', 'value': 1})
                .moveTo((690.0, 66.0))
                .lineTo((754.0, 66.0))
                .lineTo((754.0, 122.0))
                .lineTo((690.0, 122.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .tag("options")
            .add_data({'initialValue': 0, 'string_count': 2, 'shows_all_strings': False})
            .append(DATPen()
                .tag("value")
                .add_data({'ts': ['Parameter/option', 'Pre', 'FilterPosition'], 'value': 0})
                .moveTo((896.0, 620.0))
                .lineTo((992.0, 620.0))
                .lineTo((992.0, 664.0))
                .lineTo((896.0, 664.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'ts': ['Parameter/option', 'Post', 'FilterPosition'], 'value': 1})
                .moveTo((896.0, 620.0))
                .lineTo((992.0, 620.0))
                .lineTo((992.0, 664.0))
                .lineTo((896.0, 664.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .tag("options")
            .add_data({'initialValue': 0, 'string_count': 2, 'shows_all_strings': False})
            .append(DATPen()
                .tag("value")
                .add_data({'us': '+-30 dB', 'value': 0})
                .moveTo((1316.0, 620.0))
                .lineTo((1432.0, 620.0))
                .lineTo((1432.0, 664.0))
                .lineTo((1316.0, 664.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .tag("value")
                .add_data({'us': '+-15 dB', 'value': 1})
                .moveTo((1316.0, 620.0))
                .lineTo((1432.0, 620.0))
                .lineTo((1432.0, 664.0))
                .lineTo((1316.0, 664.0))
                .closePath()
                .f(bw(0.0, 0.05))))))