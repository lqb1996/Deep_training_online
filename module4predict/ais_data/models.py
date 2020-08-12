from django.db import models

# Create your models here.


class Test(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=10, verbose='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS,
                                         verbose_name='状态')

    class Meta:
        verbose_name = verbose_name_plural = '测试模型'


class Aisline(models.Model):
    NAV_STATUS_ITEMS = (
        (0, '动力航行中'),
        (1, '锚泊'),
        (2, '未受令'),
        (3, '机动性受限'),
        (4, '受吃水限制'),
        (5, '锚链系泊'),
        (6, '搁浅'),
        (7, '捕捞中'),
        (8, '风帆动力航行'),
    )

    system_timestamp = models.PositiveBigIntegerField(verbose_name='系统时间戳')
    mmsi = models.PositiveIntegerField(verbose_name='船舶MMSI,唯一标识码')
    timestamp = models.PositiveBigIntegerField(verbose_name='报文时间戳,精确到秒')
    nav_status = models.PositiveSmallIntegerField(choices=NAV_STATUS_ITEMS, verbose_name='状态')
    rot = models.SmallIntegerField(verbose_name='转向率')
    # 航行速度需要除以10（单位为：节）
    sog = models.FloatField(verbose_name='速度')
    pos_acc = models.FloatField(verbose_name='定位设备精确度')
    longitude = models.FloatField(verbose_name='纬度')
    latitude = models.FloatField(verbose_name='经度')
    # 航迹向需要除以10（单位为：度）
    cog = models.FloatField(verbose_name='航向')
    true_head = models.FloatField(verbose_name='船首向')
    eta = models.FloatField(verbose_name='预计到达时间')
    destid = models.FloatField(verbose_name='目的港ID（计算出来的）')
    srcid = models.FloatField(verbose_name='数据源标识')
    distance = models.FloatField(verbose_name='到目的港剩余距离（计算出来的）')
    speed = models.FloatField(verbose_name='平均航速（计算出来的）')
    # 吃水除以10（单位为：米）
    draught = models.FloatField(verbose_name='吃水')
    """
    船舶类型，取第一个数字，说明如下：
    2 = Wing in ground（地效翼船）
    3 = Engaged（作业船）
    4 = High Speed Craft（高速轮）
    5 = Tug, Pilot, etc（拖轮，公务船，执法艇）
    6 = Passenger Vessels（客轮）
    7 = Cargo Vessels（货轮）
    8 = Tankers（油轮）
    其它 = Others（不详）
    """
    ship_type = models.FloatField(verbose_name='船舶类型')

    class Meta:
        verbose_name = verbose_name_plural = 'AIS数据'
