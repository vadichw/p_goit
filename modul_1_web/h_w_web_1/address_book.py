�
    pÚel  �                   �D   �  G d � d�      Z  G d� de �      Z G d� de �      Zy)c                   �R   � e Zd Zd� Zed� �       Zej                  d� �       Zd� Zd� Zy)�Fieldc                 �    � d | _         || _        y �N)�_value�value��selfr   s     �T   c:\Users\а\Desktop\Vadim\repos\projects_go_it\python_web\modul_1\h_w_web_1\field.py�__init__zField.__init__   s   � ������
�    c                 �   � | j                   S r   )r   �r	   s    r
   r   zField.value   s   � ��{�{�r   c                 �4   � | j                  |�       || _        y r   )�validater   )r	   �	new_values     r
   r   zField.value
   s   � ����i� ���r   c                  �   � y r   � r   s     r
   r   zField.validate   s   � �r   c                 �,   � t        | j                  �      S r   )�strr   r   s    r
   �__str__zField.__str__   s   � ��4�;�;��r   N)	�__name__�
__module__�__qualname__r   �propertyr   �setterr   r   r   r   r
   r   r     