- (NSString* )modifyString: (NSString* )string withArray:(NSArray* )array {
    NSString* mutableString = [NSString string];
    NSArray* itemArray = [string componentsSeparatedByString:@" "];
    
    BOOL isExist;
    for (NSString* item in itemArray) {
        isExist = NO;
        for (NSString* rootItem in array) {
            if ([item hasPrefix:rootItem]) {
                mutableString = [mutableString stringByAppendingFormat:@"%@ ", rootItem];
                isExist = YES;
                break;
            }
        }
        
        if (!isExist) {
            mutableString = [mutableString stringByAppendingFormat:@"%@ ", item];
        }
    }
    
    return mutableString;
}