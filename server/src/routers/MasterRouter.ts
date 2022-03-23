import { NextFunction, Request, Response, Router } from 'express';

class MasterRouter {
    private _router = Router();

    get router() {
        return this._router;
    }

    constructor() {
        this._configure();
    }

    /**
     * Connect routes to their matching routers.
     */
    private _configure() {
        this._router.get('/', (req: Request, res: Response, next: NextFunction) => {
            console.log('api')
            res.status(200).json({ text: 'Hello'});
        });
    }
}

export = new MasterRouter().router;