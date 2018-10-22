'''
    tableview的优化方案都有哪些？
    1、cell重用：
    # 创建复用标识
    static NSString *reuseID = “reuseCellID”;
    // 缓存池中取已经创建的cell
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:reuseID];
   若能够查询到，否则，返回nil；而且需要判断if（cell == nil），才会创建Cell，
   所以：不推荐
   优化：建议使用：
   - (void)registerNib:(nullable UINib *)nib forCellReuseIdentifier:(NSString *)identifier NS_AVAILABLE_IOS(5_0);
- (void)registerClass:(nullable Class)cellClass forCellReuseIdentifier:(NSString *)identifier NS_AVAILABLE_IOS(6_0);



    2、定义一种(尽量少)类型的Cell及善用hidden隐藏(显示)subviews
    3、
    4、

'''