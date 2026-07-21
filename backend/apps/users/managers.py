from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    
    def create_user(self,full_name,email,password=None,role="MEMBER"):
        
        if not email :
            raise ValueError("Email is required")
        
        email=self.normalize_email(email)
        
        user=self.model(full_name=full_name,
                        email=email,
                        role=role)
        user.set_password(password)
        
        user.save(using=self._db)
        
        return user 
    

    def create_superuser(self,email,full_name,password=None):
        
        user=self.create_user(email=email,
            full_name=full_name,
            password=password,
            role="OWNER",
            )
        
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        
        user.save(using=self._db)
        
        return user 
    
    