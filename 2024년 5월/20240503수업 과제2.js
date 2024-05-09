let one_1 = 1;
let one_2 = 2;

if (-10000<=one_1 || one_2<=10000) {
    if (one_1 < one_2) {
        console.log('<');
    } else if (one_1 > one_2) {
        console.log(">");
    } else if (one_1 == one_2) {
        console.log('==');
    }
}

//----------------------------------------------------------

let two_1 = 100;

if (two_1 <= 100) {
    if (90 <= two_1 <= 100) {
        console.log('A')
    } else if (80 <= two_1 <= 89) {
        console.log('B')
    } else if (70 <= two_1 <= 79) {
        console.log('C')
    } else if (60 <= two_1 <= 69) {
        console.log('D')
    } else {
        console.log('F')
    } 
}

//---------------------------------------------------------

let three_1 = 2000;

if (1 <= three_1 <= 4000) {
    if (three_1%4==0) {
        if (three_%100!=0) {
            console.log(1);
        } else {
            console.log(0);
        };
    } else if (three_1%400==0) {
        console.log(1);
    } else {
        console.log(0);
    };
};

//------------------------------------------------------------

let four_1 = 12;
let four_2 = 5;

if (four_1 > 0) {
    if (four_2 > 0) {
        console.log(1);
    } else {
        console.log(4);
    };
} else {
    if (four_2 > 0) {
        console.log(2);
    } else {
        console.log(3);
    };
};

//----------------------------------------------------------

let five_1 = 10;
let five_2 = 10;

if (0<=five_1<=23 || 0 <= five_2 <= 59) {
    if (five_1 > 1) {
        if (five_2 > 45) {
            console.log((five_1),(five_2-45));
        } else; {
            console.log((five_1-1),(60-45+five_2));
        };
    } else {
        if (five_2 > 45) {
            console.log((23),(five_2-45));
        }else {
            console.log((23),(60-45+five_2));
        };
    };
};

//----------------------------------------------------------

let six_1 = 14;
let six_2 = 30;
let six_3 = 20;

if (0<=six_1<=23 || 0 <= six_2 <= 59 || 0 <= six_3 <= 1000) {
    if (six_1<23) {
        if (six_2+six_3 < 60) {
            console.log(six_1, six_2+six_3);
        } else {
            if (six_1+1, (60-six_2)+six_3);
        };
    } else {
        if (six_2+six_3 < 60) {
            console.log(six_1, six_2+six_3);
        } else {
            if (0,(60-six_2)+six_3);
        };
    };
};

//-------------------------------------------------------

let seven_1 = 3;
let seven_2 = 3;
let seven_3 = 6;

if (1 <= seven_1 <= 6 || 1 <= seven_2 <= 6 || 1 <= seven_3 <= 6 ) {
    if (seven_1 == seven_2 || seven_1 == seven_3 || seven_2 == seven_3) {
        console.log(10000+(seven_1*1000));
    } else if (seven_1 == seven_2) {
        console.log(1000+(seven_1*100));
    } else if (seven_2 == seven_3) {
        console.log(1000+(seven_2*100));
    } else if (seven_1 == seven_3) {
        console.log(1000+(seven_1*100));
    } else {
        if (seven_1 > seven_2 || seven_2 > seven_3) {
            console.log(seven_1*100);
        } else if (seven_2 > seven_1 || seven_2 > seven_3) {
            console.log(seven_2*100);
        } else {
            console.log(seven_3*100);
        };
    };
};

//------------------------------------------------------