(P()
    .data(**{})
    .append(P()
        .tag("parameter-edges")
        .data(**{})
        .moveTo((0.0, 620.0))
        .lineTo((500.0, 620.0))
        .endPath()
        .moveTo((0.0, 484.0))
        .lineTo((380.0, 484.0))
        .endPath()
        .moveTo((380.0, 484.0))
        .lineTo((380.0, 620.0))
        .endPath()
        .moveTo((0.0, 348.0))
        .lineTo((380.0, 348.0))
        .endPath()
        .moveTo((380.0, 348.0))
        .lineTo((380.0, 484.0))
        .endPath()
        .moveTo((0.0, 212.0))
        .lineTo((380.0, 212.0))
        .endPath()
        .moveTo((380.0, 212.0))
        .lineTo((380.0, 348.0))
        .endPath()
        .moveTo((500.0, 620.0))
        .lineTo((752.0, 620.0))
        .endPath()
        .moveTo((500.0, 508.0))
        .lineTo((752.0, 508.0))
        .endPath()
        .moveTo((626.0, 212.0))
        .lineTo((626.0, 508.0))
        .endPath()
        .moveTo((752.0, 620.0))
        .lineTo((880.0, 620.0))
        .endPath()
        .f(bw(0.0, 0.0))
        .s(bw(0.5))
        .sw(3))
    .append(P()
        .tag("clump-edges")
        .data(**{})
        .moveTo((500.0, 212.0))
        .lineTo((500.0, 692.0))
        .endPath()
        .moveTo((752.0, 212.0))
        .lineTo((752.0, 692.0))
        .endPath()
        .moveTo((0.0, 212.0))
        .lineTo((880.0, 212.0))
        .endPath()
        .moveTo((0.0, 104.0))
        .lineTo((880.0, 104.0))
        .endPath()
        .f(bw(0.0, 0.0))
        .s(bw(0.25))
        .sw(5))
    .append(P()
        .tag("sidebar")
        .data(**{})
        .moveTo((880.0, 44.0))
        .lineTo((1004.0, 44.0))
        .lineTo((1004.0, 692.0))
        .lineTo((880.0, 692.0))
        .closePath()
        .f(bw(0.5)))
    .append(P()
        .tag("advbar")
        .data(**{})
        .moveTo((0, 0))
        .lineTo((2, 0))
        .lineTo((2, 2))
        .lineTo((0, 2))
        .closePath()
        .f(bw(0.75)))
    .append(P()
        .tag("labels")
        .data(**{})
        .append(P()
            .tag("param")
            .data(**{'align': [6, 3], 'ts': ['ParamLabel/text', 'Frequency', None]})
            .moveTo((6.0, 496.0))
            .lineTo((374.0, 496.0))
            .lineTo((374.0, 560.0))
            .lineTo((6.0, 560.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(P()
            .tag("param")
            .data(**{'align': [6, 3], 'ts': ['ParamLabel/text', 'Slope', None]})
            .moveTo((6.0, 360.0))
            .lineTo((374.0, 360.0))
            .lineTo((374.0, 424.0))
            .lineTo((6.0, 424.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(P()
            .tag("param")
            .data(**{'align': [6, 3], 'ts': ['ParamLabel/text', 'Resonance', None]})
            .moveTo((6.0, 224.0))
            .lineTo((374.0, 224.0))
            .lineTo((374.0, 288.0))
            .lineTo((6.0, 288.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(P()
            .tag("param")
            .data(**{'align': [6, 3], 'ts': ['ParamLabel/text', 'Mix', None]})
            .moveTo((386.0, 224.0))
            .lineTo((494.0, 224.0))
            .lineTo((494.0, 288.0))
            .lineTo((386.0, 288.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(P()
            .tag("param")
            .data(**{'align': [6, 5], 'ts': ['ClumpLabel/text', 'LIM/SAT', None]})
            .moveTo((514.0, 620.0))
            .lineTo((700.0, 620.0))
            .lineTo((700.0, 692.0))
            .lineTo((514.0, 692.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(P()
            .tag("param")
            .data(**{'align': [6, 3], 'ts': ['ParamLabel/text', 'Threshold', None]})
            .moveTo((506.0, 224.0))
            .lineTo((620.0, 224.0))
            .lineTo((620.0, 288.0))
            .lineTo((506.0, 288.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(P()
            .tag("param")
            .data(**{'align': [6, 3], 'ts': ['ParamLabel/text', 'Color', None]})
            .moveTo((632.0, 224.0))
            .lineTo((746.0, 224.0))
            .lineTo((746.0, 288.0))
            .lineTo((632.0, 288.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(P()
            .tag("param")
            .data(**{'align': [6, 5], 'ts': ['ParamLabel/text', 'DRY', None]})
            .moveTo((6.0, 104.0))
            .lineTo((174.0, 104.0))
            .lineTo((174.0, 212.0))
            .lineTo((6.0, 212.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(P()
            .tag("param")
            .data(**{'align': [6, 5], 'us': 'LOHI'})
            .moveTo((706.0, 104.0))
            .lineTo((874.0, 104.0))
            .lineTo((874.0, 212.0))
            .lineTo((706.0, 212.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(P()
            .tag("param")
            .data(**{'align': [6, 3], 'ts': ['ParamLabel/text', 'Lim/Sat\nAuto Gain', None]})
            .moveTo((1010.0, 522.0))
            .lineTo((1238.0, 522.0))
            .lineTo((1238.0, 586.0))
            .lineTo((1010.0, 586.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(P()
            .tag("param")
            .data(**{'align': [6, 3], 'ts': ['ParamLabel/text', 'Lim/Sat\nStereo Link', None]})
            .moveTo((1010.0, 332.0))
            .lineTo((1238.0, 332.0))
            .lineTo((1238.0, 396.0))
            .lineTo((1010.0, 396.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(P()
            .tag("param")
            .data(**{'align': [6, 3], 'ts': ['ParamLabel/text', 'Filter\nGlide Time', None]})
            .moveTo((1010.0, 132.0))
            .lineTo((1238.0, 132.0))
            .lineTo((1238.0, 196.0))
            .lineTo((1010.0, 196.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(P()
            .tag("clump")
            .data(**{'align': [6, 5], 'ts': ['ClumpLabel/text', 'OUT', None]})
            .moveTo((766.0, 620.0))
            .lineTo((866.0, 620.0))
            .lineTo((866.0, 692.0))
            .lineTo((766.0, 692.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(P()
            .tag("options")
            .data(**{'initialValue': 0, 'string_count': 4, 'shows_all_strings': True})
            .append(P()
                .tag("value")
                .data(**{'align': [6, 5], 'us': 'LO', 'value': 0})
                .moveTo((48.0, 634.0))
                .lineTo((131.0, 634.0))
                .lineTo((131.0, 678.0))
                .lineTo((48.0, 678.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(P()
                .tag("value")
                .data(**{'align': [6, 5], 'us': 'HI', 'value': 1})
                .moveTo((143.0, 634.0))
                .lineTo((226.0, 634.0))
                .lineTo((226.0, 678.0))
                .lineTo((143.0, 678.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(P()
                .tag("value")
                .data(**{'align': [6, 5], 'us': 'BP', 'value': 2})
                .moveTo((238.0, 634.0))
                .lineTo((321.0, 634.0))
                .lineTo((321.0, 678.0))
                .lineTo((238.0, 678.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(P()
                .tag("value")
                .data(**{'align': [6, 5], 'ts': ['Parameter/option', 'Off', None], 'value': 3})
                .moveTo((369.0, 634.0))
                .lineTo((452.0, 634.0))
                .lineTo((452.0, 678.0))
                .lineTo((369.0, 678.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(P()
            .tag("options")
            .data(**{'initialValue': 0, 'string_count': 0, 'shows_all_strings': False}))
        .append(P()
            .tag("options")
            .data(**{'initialValue': 0, 'string_count': 2, 'shows_all_strings': True})
            .append(P()
                .tag("value")
                .data(**{'align': [6, 5], 'ts': ['Parameter/option', 'Off', None], 'value': 0})
                .moveTo((1040.0, 411.0))
                .lineTo((1118.0, 411.0))
                .lineTo((1118.0, 455.0))
                .lineTo((1040.0, 455.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(P()
                .tag("value")
                .data(**{'align': [6, 5], 'ts': ['Parameter/option', 'On', None], 'value': 1})
                .moveTo((1130.0, 411.0))
                .lineTo((1208.0, 411.0))
                .lineTo((1208.0, 455.0))
                .lineTo((1130.0, 455.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(P()
            .tag("options")
            .data(**{'initialValue': 250, 'string_count': 0, 'shows_all_strings': False}))))