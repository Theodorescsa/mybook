# Lấy một đối tượng CategoryBookModel
category = CategoryBookModel.objects.get(pk=1)  # Thay 1 bằng ID thực tế của đối tượng bạn muốn lấy

# Lấy giá trị của trường 'id' từ đối tượng 'CategoryBookModel'
category_id = category.id