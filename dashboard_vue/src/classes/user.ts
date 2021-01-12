import {Role} from '@/classes/role'
import {Entity} from '@/interfaces/entity'

export class User implements Entity {
    id: number;
    username: string;
    email: string;
    role: Role;
    permissions: string[];


    constructor(id:number=0, username:string="", email:string="", role:Role = new Role(), permissions: string[]= []){
        this.id = id
        this.username = username
        this.email = email
        this.role = role
        this.permissions = permissions

    }

    canView(page: string) {
        return this.permissions.some(p => p === `view_${page}`)
    }

    canEdit(page:string){
        return this.permissions.some(p =>  p === `edit_${page}`)
    }

}