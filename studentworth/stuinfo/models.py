from django.db import models

# Create your models here.
class classinfo(models.Model):
    """    班级信息表    """
    classinfo_type_choice = (
        ('classid', '班级ID'),
        ('classname', '班级名称'),
        ('classcategory', '文理科'),
        ('classtype', '班级类型'),
        ('classintroduction', '学期'),
    )

    classinfo_status = (
        (0, '高一（上）学期'),
        (1, '高一（下）学期'),
        (2, '高二（上）学期'),
        (3, '高二（下）学期'),
        (4, '高三（上）学期'),
        (5, '高三（下）学期'),
        )

    
    memo = models.TextField(null=True, blank=True, verbose_name='备注')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='批准日期')
    m_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    def __str__(self):
        return '<%s>  %s' % (self.get_asset_type_display(), self.name)

    class Meta:
        verbose_name = '班级信息表'
        verbose_name_plural = "班级信息表"
        ordering = ['-c_time']