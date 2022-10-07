function isMatch(s: string, p: string): boolean {
    count:Number;
    tem:String;
    if(p.length==0){
        return s.length==0;
    }
    if(p.length==1){
        return s.length==1&&(p[0]==s[0]||p[0]=='.');
    }
    if(p[1]!='*'){
        if(s.length==0){
            return false;
        }
        return (p[0]==s[0]||p[0]=='.')&&isMatch(s.substring(1),p.substring(1));
    }
    while(s.length>0&&(p[0]==s[0]||p[0]=='.')){
        if(isMatch(s,p.substring(2))){
            return true;
        }
        s=s.substring(1);
    }
    return isMatch(s,p.substring(2));
    
}